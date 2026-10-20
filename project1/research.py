"""Dated source facts and transparent judgment inputs; no runtime web calls."""
COHR_FILING = 'https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm'
FN_FILING = 'https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/fn-20260626.htm'
TREASURY = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202609&type=daily_treasury_yield_curve'
ERP_SOURCE = 'https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm'

HISTORICAL = {
    'source':COHR_FILING,'period':'FY ended 2026-06-30','units':'USD millions',
    'revenue':7118.181,'cogs':4449.141,'rd':722.952,'sga':1044.566,
    'pretax':847.733,'interest':190.267,'other_income':140.139,
    'restructuring':63.390,'held_for_sale_impairment':64.404,'business_sale_gain':124.133,
    'cfo':79.514,'cfi':-1413.724,'cff':1477.076,'fx':-7.383,
    'opening_cash_including_restricted':1632.913,'closing_cash_including_restricted':1768.396,
    'cash_capex':1102.909,'intangible_purchases':7.174,
    'depreciation':241.561,'amortization':280.334,'sbc':186.468,
}


def wacc_build(price=271.17, shares=195.832246):
    rf, beta, erp, kd, tax = .05, 1.75, .0414, .055, .20
    common_equity = price*shares
    nci, debt = 334.705, 3257.482+14.233
    equity = common_equity+nci
    ke = rf+beta*erp
    equity_weight = equity/(equity+debt)
    result = equity_weight*ke+(1-equity_weight)*kd*(1-tax)
    return {'risk_free': rf, 'risk_free_date':'2026-09-15', 'risk_free_source':TREASURY,
            'equity_risk_premium':erp,'erp_date':'2026-09-01','erp_source':ERP_SOURCE,
            'beta':beta,'beta_basis':'Analyst judgment; not a measured historical regression. Cyclical optical demand and concentrated AI customers justify above-market risk; 1.25–2.00 is a challenge band, not a statistical interval.',
            'pretax_debt_cost':kd,'debt_cost_basis':'5.5% judgment near filing interest/average debt proxy; current marginal credit yield is not observed.',
            'tax_rate':tax,'tax_basis':'20% normalized judgment retained from pro-forma; not FY2026 effective rate.',
            'cost_of_equity':ke,'common_market_equity':common_equity,'nci_equity_proxy':nci,
            'debt_including_finance_leases':debt,'equity_weight':equity_weight,
            'debt_weight':1-equity_weight,'calculated_wacc':result,
            'rounded_panel_wacc_pct':round(result*100,1),
            'classification':'Calculated from sourced rate/ERP and explicit beta/debt-cost/tax judgments; not a fully observed WACC.'}


def peer_analysis(target_net_claims):
    # Same cash policy: retain operating cash equal to 300 / COHR sales;
    # subtract remaining cash and ST investments for BOTH companies.
    operating_cash_ratio = 300/7118.181
    inputs = {
        'COHR':{'price':271.17,'shares':195.832246,'revenue':7118.181,'ebit':897.861,
                'da':521.895,'eps':4.12,'cash':1162.018,'investments':825.,
                'gross_debt':3257.482,'finance_leases':14.233,'nci':334.705,'pension_deficit':49.,
                'balance_date':'2026-06-30','shares_date':'2026-08-10','fy_end':'2026-06-30','source':COHR_FILING},
        'FN':{'price':374.91,'shares':35.834864,'revenue':4641.097,'ebit':462.887,
              'da':68.371,'eps':13.05,'cash':346.711,'investments':528.344,
              'gross_debt':0.,'finance_leases':0.,'nci':0.,'pension_deficit':0.,
              'balance_date':'2026-06-26','shares_date':'2026-06-26','fy_end':'2026-06-26','source':FN_FILING}}
    rows={}
    for ticker,x in inputs.items():
        market_cap=x['price']*x['shares']
        retained=x['revenue']*operating_cash_ratio
        claims=x['gross_debt']+x['finance_leases']+x['nci']+x['pension_deficit']-(x['cash']+x['investments']-retained)
        ev=market_cap+claims
        rows[ticker]={**x,'market_cap':market_cap,'operating_cash_retained':retained,
                      'net_claims':claims,'enterprise_value':ev,'pe':x['price']/x['eps'],
                      'ev_sales':ev/x['revenue'],'ebitda':x['ebit']+x['da'],
                      'ev_ebitda':ev/(x['ebit']+x['da'])}
    peer,target=rows['FN'],rows['COHR']
    references={
        'reported_pe':peer['pe']*target['eps'],
        'ev_sales':(peer['ev_sales']*target['revenue']-target_net_claims)/target['shares'],
        'reported_ev_ebitda':(peer['ev_ebitda']*target['ebitda']-target_net_claims)/target['shares']}
    return {'policy_date':'2026-09-15','price_date':'2026-09-15','currency':'USD',
            'policy':'Existing prior policy retained: more than one continent; >=50% annual datacenter/communications sales without double counting; market cap >=$5bn. Optical manufacturing/capital intensity are supporting characteristics.',
            'policy_check':'FN multi-continent operations, 81.2% qualifying revenue and ~$13.43bn market cap using June shares support admission. Exact September 15 share count remains a timing limitation. LITE annual qualifying mix remains unverified; do not call it a verified policy pass.',
            'cash_policy':f'Retain {operating_cash_ratio:.8%} of annual sales for both companies; exclude operating leases from debt because lease costs remain operating expenses.',
            'rows':rows,'single_peer_references_per_share':references,
            'limitations':['FN contract manufacturing differs from COHR product ownership, R&D and margins; one peer does not establish a diversified range.',
                           'Annual reported GAAP earnings; not forward or adjusted EPS. COHR includes unusual items; P/E is a qualified cross-check.',
                           'EBITDA = reported operating EBIT + reported D&A; SBC retained. Market-cap shares are dated actual shares; EPS shares are annual diluted averages by definition.',
                           'Zero FN finance lease/pension/NCI claims follows disclosed balance-sheet scope; no separate strategic equity-investment value is added for either company.',
                           'Prices retained from prior research; September 15 historical rows corroborated during final preparation. Mixed market/financial dates are disclosed.',
                           'No transaction multiple adopted: company divestitures/control transactions lack a sufficiently comparable target-wide denominator and synergy/timing adjustment.'],
            'sources':[FN_FILING,COHR_FILING,'https://investor.fabrinet.com/node/13666',
                       'https://stockanalysis.com/stocks/cohr/history/','https://www.investing.com/equities/fabrinet-historical-data']}


SCENARIOS = {
    'Low: demand slowdown with investment restraint':{
        'controls':{'growth_shift_pp':-5,'margin_shift_pp':-2,'capex_shift_pp':-1,'wacc_pct':13,'terminal_growth_pct':2},
        'cause':'Slower AI orders/pricing pressure reduce growth and margin; management lowers capex intensity 1 pp. This funding response is necessary to the coherent low case, not guaranteed. The sticky-capex stress is preserved separately.'},
    'Base: growth fades and manufacturing improves':{
        'controls':{},'cause':'Original growth/margin/reinvestment forecast retained; dated, judgment-dependent WACC replaces the placeholder.'},
    'High: stronger demand plus execution and cash discipline':{
        'controls':{'growth_shift_pp':5,'margin_shift_pp':2,'capex_shift_pp':-.5,'inventory_shift_days':-15,'wacc_pct':10,'terminal_growth_pct':3.5},
        'cause':'Demand growth and product mix improve; better utilization reduces capex intensity 0.5 pp and ending inventory days by 15. This case requires efficient use of installed capacity; it is not growth without reinvestment.'},
    'Stress: slowdown with sticky investment (not executable)':{
        'controls':{'growth_shift_pp':-5,'margin_shift_pp':-2,'capex_shift_pp':1,'wacc_pct':13,'terminal_growth_pct':2},
        'cause':'Growth and margin disappoint while committed capacity spending stays high. Retained to expose financing shortfalls; not included in the passing-case valuation range.'},
}
