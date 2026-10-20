"""Project 1 signed-FCFF integration. Standard library only; lab source unchanged.

Run from repository root: python3 project1/engine.py
Outputs are provisional until the assumptions and outstanding evidence are reviewed.
"""
from copy import deepcopy
from datetime import date
import hashlib
import importlib.util
import json
from math import isfinite
from pathlib import Path
from research import wacc_build, peer_analysis, SCENARIOS, HISTORICAL

ROOT = Path(__file__).resolve().parents[1]
LAB_PATH = ROOT / 'Pro-Forma Financial Statements/proforma.COHR.py'
spec = importlib.util.spec_from_file_location('cohr_original_lab', LAB_PATH)
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

VALUATION_DATE = '2026-09-15'
INFORMATION_CUTOFF = VALUATION_DATE
MARKET_PRICE = 271.17
SHARES = 195.832246  # August 10 actual common shares, millions; NOT diluted EPS shares.
NCI = 334.705  # June 30 book-value proxy for minority claims.
MINIMUM_CASH = 300.0  # Existing analyst judgment; retained as operating cash.
WACC_BUILD = wacc_build(MARKET_PRICE, SHARES)

# Bounds on shifts are absolute percentage points; inventory shift is days.
# Growth/margin bounds retain Nicolas's prior lab choices. Other bounds are
# provisional analyst stress ranges requiring review, not confidence intervals.
DRIVERS = {
    'growth_shift_pp': {'base': 0.0, 'min': -5.0, 'max': 5.0, 'unit': 'pp', 'step': .5},
    'margin_shift_pp': {'base': 0.0, 'min': -2.0, 'max': 2.0, 'unit': 'pp', 'step': .25},
    'capex_shift_pp': {'base': 0.0, 'min': -2.0, 'max': 2.0, 'unit': 'pp', 'step': .25},
    'inventory_shift_days': {'base': 0.0, 'min': -30.0, 'max': 30.0, 'unit': 'days', 'step': 5.0},
    'wacc_pct': {'base': WACC_BUILD['rounded_panel_wacc_pct'], 'min': 9.0, 'max': 13.0, 'unit': '%', 'step': .1},
    'terminal_growth_pct': {'base': 3.0, 'min': 2.0, 'max': 4.0, 'unit': '%', 'step': .25},
}
LIMITATIONS = [
    'WACC build uses September 15 Treasury 5.00%, September 1 ERP 4.14%, and judgment beta 1.75 / debt cost 5.5% / tax 20%; beta is not a regression estimate. Rounded base WACC is 11.8%.',
    'June 30 cash, debt and NCI and August 10 common shares are proxies at September 15; no actual interim balance sheet is asserted.',
    'Actual common shares are used, not historical diluted EPS weighted-average shares. SBC is retained as an economic expense without a cash add-back or forecast share issuance.',
    'FY2027 DCF uses a 288/365 remaining-year fraction under uniform cash generation; annual statements still show the full fiscal year. Seasonality and interim actual cash flows are not modeled.',
    'Terminal reinvestment changes to g times closing modeled operating capital; this transition is an assumption, not company guidance.',
    'Financing failures are shown separately from operating value: conditional DCF diagnostics do not make an unfunded scenario executable.',
    'No new acquisitions, divestitures, refinancing, NCI earnings/distributions or incremental capacity constraints beyond the inherited lab conventions.',
    'Debt maturity table conflicts with some narrative maturity dates; annual funding results follow the table and are conditional. Springing maturities, intrayear timing and covenants are not modeled.',
    'The August 2026 ~$945m subsidiary facility was known before the cutoff but is excluded from parent funding capacity because its uses/guarantees are restricted. Funding failures are not company insolvency forecasts.',
    'Gross debt and NCI book value proxy market claims; finance leases and $49m pension deficits are deducted separately. Operating lease costs remain expenses; strategic equity assets receive no separate value without a verified realizable amount.',
]


def validate_controls(controls):
    unknown = set(controls) - set(DRIVERS)
    if unknown:
        raise ValueError(f'Unknown controls: {sorted(unknown)}')
    merged = {k: d['base'] for k, d in DRIVERS.items()}
    for key, value in controls.items():
        d = DRIVERS[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
            raise ValueError(f'{key}: finite numeric value required')
        if not d['min'] <= value <= d['max']:
            raise ValueError(f"{key}: outside defended panel range [{d['min']}, {d['max']}]")
        merged[key] = float(value)
    return merged


def discounted_fcff(path, wacc, growth, terminal_fcff, times, first_fraction=1.0):
    """Signed operating cash flows; no max(0, FCFF) clipping."""
    values = [*path, wacc, growth, terminal_fcff, *times, first_fraction]
    if not all(isfinite(x) for x in values) or len(path) != len(times):
        raise ValueError('Finite cash flows and matching discount times required')
    if not 0 <= growth < wacc or wacc <= 0 or not 0 < first_fraction <= 1:
        raise ValueError('Require 0 <= terminal growth < positive WACC and valid stub')
    if terminal_fcff <= 0:
        raise ValueError('Positive sustainable terminal FCFF required')
    cash_flows = list(path)
    cash_flows[0] *= first_fraction
    explicit = sum(cf / (1 + wacc)**t for cf, t in zip(cash_flows, times))
    terminal_value = terminal_fcff / (wacc - growth)
    terminal_pv = terminal_value / (1 + wacc)**times[-1]
    return {'dcf_cash_flows': cash_flows, 'discount_times': times,
            'explicit_pv': explicit, 'terminal_value': terminal_value,
            'terminal_pv': terminal_pv, 'enterprise_value': explicit + terminal_pv,
            'terminal_share': terminal_pv / (explicit + terminal_pv)}


def run(controls=None):
    c = validate_controls(controls or {})
    a = deepcopy(lab.ASSUMPTIONS)
    for field, key in [('growth', 'growth_shift_pp'), ('gross_margin', 'margin_shift_pp'),
                       ('capex_ratios', 'capex_shift_pp')]:
        a[field] = tuple(x + c[key]/100 for x in a[field])
    a['inventory_days'] += c['inventory_shift_days']
    a['wacc'] = c['wacc_pct']/100
    a['terminal_growth'] = c['terminal_growth_pct']/100
    rows = lab.project(assumptions=a)
    checks = []
    opening = lab.totals(deepcopy(lab.OPENING))
    checks.append({'check': 'Opening assets reconcile to filing', 'pass': abs(opening['assets']-18299.852)<1e-7,
                   'gap': opening['assets']-18299.852, 'unit': 'USD million'})
    checks.append({'check': 'Opening liabilities reconcile to filing', 'pass': abs(opening['liabilities']-7061.652)<1e-7,
                   'gap': opening['liabilities']-7061.652, 'unit': 'USD million'})
    h=HISTORICAL
    reported_ebit=h['pretax']+h['interest']-h['other_income']
    normalized_ebit=h['revenue']-h['cogs']-h['rd']-h['sga']
    historical_cash_gap=(h['opening_cash_including_restricted']+h['cfo']+h['cfi']+h['cff']+h['fx']
                         -h['closing_cash_including_restricted'])
    normalization_gap=(reported_ebit+h['restructuring']+h['held_for_sale_impairment']
                       -h['business_sale_gain']-normalized_ebit)
    for name,gap in [('Historical cash-flow ties including restricted cash',historical_cash_gap),
                     ('Opening revenue ties to filing',opening['revenue']-h['revenue']),
                     ('Normalized core EBIT bridge',normalization_gap)]:
        checks.append({'check':name,'pass':abs(gap)<1e-7,'gap':gap,'unit':'USD million'})
    for row in rows:
        row['fcff'] = (row['operating_income']*(1-a['tax_rate']) + row['depreciation']
                       + row['amortization'] + row['impairment'] - row['change_inventory']
                       - row['change_other_wc'] - row['capex'] - row['intangible_purchases'])
        # Independent CFO identity valid for the current positive taxable-income cases.
        via_cfo = (row['operating_cash_flow'] + row['cash_interest']*(1-a['tax_rate'])
                   - row['debt_cost_amortization']*a['tax_rate']
                   - row['capex'] - row['intangible_purchases'])
        row['fcff_identity_gap'] = row['fcff']-via_cfo
        for key in (*lab.ZERO_CHECKS, 'fcff_identity_gap', 'cash_floor_shortfall',
                    'revolver_limit_excess', 'negative_balance_check'):
            gap = row[key]
            checks.append({'check': f"FY{row['year']} {key}", 'pass': abs(gap)<1e-7,
                           'gap': gap, 'unit': 'USD million'})
    last = rows[-1]
    g = a['terminal_growth']
    capital = sum(last[k] for k in ['ppe', 'intangibles', 'inventory', 'other_operating_assets']) - last['operating_liabilities']
    terminal_nopat = last['operating_income']*(1+g)*(1-a['tax_rate'])
    terminal_reinvestment = capital*g
    terminal_fcff = terminal_nopat-terminal_reinvestment
    first_fraction = (date(2027,6,30)-date.fromisoformat(VALUATION_DATE)).days/365
    times = [first_fraction+i for i in range(5)]
    v = discounted_fcff([r['fcff'] for r in rows], a['wacc'], g, terminal_fcff, times, first_fraction)
    bridge = {'cash': lab.OPENING['cash'], 'operating_cash_retained': MINIMUM_CASH,
              'short_term_investments': lab.OPENING['short_term_investments'],
              'gross_debt': lab.OPENING['gross_debt'], 'nci': NCI, 'preferred': 0.0,
              'finance_leases': 14.233, 'pension_deficit': 49.0}
    bridge['excess_cash_and_investments'] = bridge['cash']-MINIMUM_CASH+bridge['short_term_investments']
    bridge['net_claims'] = (bridge['gross_debt']+NCI+bridge['preferred']+bridge['finance_leases']
                            +bridge['pension_deficit']-bridge['excess_cash_and_investments'])
    v.update({'equity_value': v['enterprise_value']-bridge['net_claims'],
              'terminal_nopat': terminal_nopat, 'terminal_reinvestment': terminal_reinvestment,
              'terminal_fcff': terminal_fcff, 'terminal_operating_capital': capital})
    v['per_share'] = v['equity_value']/SHARES
    equity_back = v['equity_value'] + bridge['net_claims']
    checks.append({'check': 'Enterprise-equity bridge', 'pass': abs(equity_back-v['enterprise_value'])<1e-7,
                   'gap': equity_back-v['enterprise_value'], 'unit': 'USD million'})
    target_ev = MARKET_PRICE*SHARES+bridge['net_claims']
    required_terminal_fcff = (target_ev-v['explicit_pv'])*(1+a['wacc'])**times[-1]*(a['wacc']-g)
    v['reverse_dcf'] = {'target_price': MARKET_PRICE, 'held_fixed': 'explicit FCFF, WACC, g and equity bridge',
                         'required_terminal_fcff': required_terminal_fcff,
                         'multiple_of_base_terminal_fcff': required_terminal_fcff/terminal_fcff,
                         'interpretation': 'Market-implied terminal cash flow, not a forecast or proof of mispricing.'}
    historical_bands = {
        'growth':(-.0877,5810.115/4707.688-1),
        'gross_margin':((4707.688-3251.724)/4707.688,(7118.181-4449.141)/7118.181),
        'capex_ratios':(346.816/4707.688,1102.909/7118.181),
    }
    history_checks = []
    for key,(lower,upper) in historical_bands.items():
        outside=[lab.YEARS[i] for i,x in enumerate(a[key]) if not lower-1e-8<=x<=upper+1e-8]
        history_checks.append({'driver':key,'historical_min':lower,'historical_max':upper,
                               'forecast_path':a[key],'within_history':not outside,'outside_years':outside,
                               'classification':'Assumption challenge; not an accounting/funding failure',
                               'explanation':'Forward departures are deliberate analyst judgments; rationale and reversal evidence are in docs/assumption-challenge-record.md.'})
    return {'valuation_date': VALUATION_DATE, 'information_cutoff': INFORMATION_CUTOFF,
            'status': 'PROVISIONAL - assumption review and further evidence required',
            'currency': 'USD', 'financial_units': 'millions', 'share_basis': 'actual common shares',
            'shares_million': SHARES, 'market_price': MARKET_PRICE, 'controls': c, 'assumptions': a,
            'wacc_build': WACC_BUILD,
            'historical':{**h,'reported_operating_ebit':reported_ebit,'normalized_core_ebit':normalized_ebit},
            'opening': opening, 'statements': rows, 'valuation': v, 'bridge': bridge,
            'checks': checks, 'all_checks_pass': all(x['pass'] for x in checks),
            'historical_band_checks':history_checks,
            'limitations': LIMITATIONS,
            'lab_source_sha256': hashlib.sha256(LAB_PATH.read_bytes()).hexdigest()}


def sensitivity():
    """Same base, independent endpoint runs; repeat at half range to test ranking."""
    base = run()
    result = []
    for scale in [1.0, .5]:
        for key, d in DRIVERS.items():
            low = run({key: d['base']+(d['min']-d['base'])*scale})
            high = run({key: d['base']+(d['max']-d['base'])*scale})
            result.append({'driver': key, 'range_scale': scale,
                           'low_input': low['controls'][key], 'base_input': d['base'], 'high_input': high['controls'][key],
                           'low_value': low['valuation']['per_share'], 'base_value': base['valuation']['per_share'],
                           'high_value': high['valuation']['per_share'],
                           'low_ebit': low['statements'][-1]['operating_income'],
                           'high_ebit': high['statements'][-1]['operating_income'],
                           'low_fcff': low['statements'][-1]['fcff'], 'high_fcff': high['statements'][-1]['fcff'],
                           'low_valid': low['all_checks_pass'], 'high_valid': high['all_checks_pass'],
                           'conditional_value_span': abs(high['valuation']['per_share']-low['valuation']['per_share'])})
    return result


def full_report():
    r = run()
    r['sensitivity'] = sensitivity()
    summaries=[]
    base_metrics={'ebit':r['statements'][-1]['operating_income'],
                  'fcff':r['statements'][-1]['fcff'],'value':r['valuation']['per_share']}
    for s in r['sensitivity']:
        item={'driver':s['driver'],'range_scale':s['range_scale'],
              'valid_endpoints':[side for side in ['low','high'] if s[side+'_valid']]}
        for metric,base_value in base_metrics.items():
            values=[base_value]+[s[side+'_'+metric] for side in item['valid_endpoints']]
            item[metric+'_valid_span']=max(values)-min(values)
        summaries.append(item)
    r['sensitivity_valid_spans']=summaries
    r['wacc_growth_grid'] = [{'wacc_pct':w,'g_pct':g,'per_share':run({'wacc_pct':w,'terminal_growth_pct':g})['valuation']['per_share']}
                              for w in [9,10,11,11.8,12,13] for g in [2,3,4]]
    r['scenarios'] = []
    for name, s in SCENARIOS.items():
        case = run(s['controls'])
        r['scenarios'].append({'name':name,'cause':s['cause'],'controls':case['controls'],
                               'per_share':case['valuation']['per_share'],'valid':case['all_checks_pass'],
                               'terminal_share':case['valuation']['terminal_share'],
                               'failed_checks':[x for x in case['checks'] if not x['pass']],
                               'statements':case['statements']})
    passing = [s['per_share'] for s in r['scenarios'] if s['valid']]
    r['passing_scenario_range'] = [min(passing),max(passing)]
    r['peers'] = peer_analysis(r['bridge']['net_claims'])
    # Terminal return stress holds five-year forecast and market bridge fixed.
    v=r['valuation'];w=r['assumptions']['wacc'];g=r['assumptions']['terminal_growth']
    r['terminal_roic_stress'] = []
    for roic in [.08,.12,.16]:
        terminal_fcff=v['terminal_nopat']*(1-g/roic)
        ev=v['explicit_pv']+terminal_fcff/(w-g)/(1+w)**v['discount_times'][-1]
        r['terminal_roic_stress'].append({'roic':roic,'terminal_fcff':terminal_fcff,
                                         'per_share':(ev-r['bridge']['net_claims'])/SHARES})
    return r


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT/'outputs')
    args = parser.parse_args()
    output = args.output_dir
    output.mkdir(parents=True, exist_ok=True)
    result = full_report()
    (output/'project1-base.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    v=result['valuation']
    text = [f'# COHR provisional integrated FCFF output', '', f'Valuation date and information cutoff: {VALUATION_DATE}.',
            'Generated during AI-assisted final preparation; not an AI-closed run or a historical submission receipt.', '',
            f"Base diagnostic: ${v['per_share']:.2f} per actual common share; WACC {result['controls']['wacc_pct']:.1f}%, g 3% (judgment-dependent).",
            f"Enterprise value: ${v['enterprise_value']:,.3f}m; common equity: ${v['equity_value']:,.3f}m.",
            f"Net claims: ${result['bridge']['net_claims']:,.3f}m; shares: {SHARES:.6f}m.",
            f"Terminal PV / EV: {v['terminal_share']:.2%}. Checks: {'PASS' if result['all_checks_pass'] else 'FAIL'}.", '',
            '| Fiscal year | Revenue | EBIT | CFO | PP&E capex | Signed FCFF | Closing cash |',
            '|---|---:|---:|---:|---:|---:|---:|']
    for r in result['statements']:
        text.append('| '+str(r['year'])+' | '+' | '.join(f'{r[k]:,.3f}' for k in ['revenue','operating_income','operating_cash_flow','capex','fcff','cash'])+' |')
    text += ['', '## Causal scenarios', '', '| Scenario | Conditional value / share | Funding/articulation |', '|---|---:|---|']
    for s in result['scenarios']:
        text.append(f"| {s['name']} | ${s['per_share']:.2f} | {'PASS' if s['valid'] else 'FAIL; excluded'} |")
    text += ['', f"Passing-case DCF range: ${result['passing_scenario_range'][0]:.0f}–${result['passing_scenario_range'][1]:.0f}/share; a scenario range, not a confidence interval.",
             '', '## Single-peer cross-checks', '', *[f'- {k}: ${v:.2f}/share (qualified single-peer reference).' for k,v in result['peers']['single_peer_references_per_share'].items()]]
    text += ['', 'Full inputs, all three statements, checks, bridge, WACC–growth grid, reverse DCF, and one-at-a-time sensitivities are visible in `project1-base.json`.', '',
             '## Limitations', '', *['- '+x for x in LIMITATIONS]]
    (output/'project1-base.md').write_text('\n'.join(text)+'\n')
    print('\n'.join(text[:10]))
    print(f'Visible outputs: {output}')


if __name__ == '__main__':
    main()
