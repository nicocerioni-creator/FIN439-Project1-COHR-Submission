"""Build review drafts from executed numbers; never alters Edition A or lab files."""
import csv
import json
from pathlib import Path
from engine import full_report, ROOT
from research import COHR_FILING, FN_FILING, TREASURY, ERP_SOURCE


def main():
    r=full_report();v=r['valuation'];p=r['peers'];w=r['wacc_build']
    low,high=r['passing_scenario_range'];draft_range=f'${low:.0f}–${high:.0f}'
    docs=ROOT/'docs';docs.mkdir(exist_ok=True)
    memo=f'''# COHR — Watch / defer; do not initiate at the reference price

**Analyst:** Nicolas Cerioni. Recommendation and operating thesis reviewed during final preparation; risk emphasis updated October 19, 2026.

**User:** Buy-side investment committee; fund holds no position. **Security:** NYSE: COHR common stock. **Valuation / information cutoff:** September 15, 2026. **Decision horizon:** 3–5 years. USD; actual common-share basis. Prepared October 19 using dated historical evidence; no later operating event is used to support the September 15 thesis.

**Committee ask.** Keep COHR on watch and authorize no initiation at the saved **$271.17** reference price. Passing causal DCF cases span **{draft_range}/share**, with a base diagnostic near **${v['per_share']:.0f}**. Single-peer references span roughly **$90–$164** across different definitions; they corroborate valuation risk but are not averaged into the DCF. These are conditional estimates, not a confidence interval or a short recommendation.

**Principal risks — why the fund should wait.**

- **Capacity spending may not earn its expected return.** The thesis depends on continued AI-infrastructure investment generating orders and sufficient utilization of COHR's expanded capacity. If that spending cycle slows after COHR commits capital, excess capacity and inventory can depress manufacturing margins and cash returns while debt obligations remain. Strong industry growth does not guarantee that COHR's individual projects pay off; refinancing, asset sales or dilution could become necessary.
- **Cash generation currently provides little cushion.** FY2026 operating cash flow was positive but only **$79.514m**, about **1.1% of $7.118bn revenue**. Cash PP&E capex of **$1,102.909m** left **negative $1,023.395m simple FCF**. This is CFO less PP&E capex, not FCFF. Growth investment may explain the cash use, but its eventual payoff must be demonstrated rather than assumed.
- **Concentration can increase customer negotiating leverage.** Two customers accounted for **20% and 12% of revenue — 32% combined**; their names are not given in that disclosure. **Datacenter & Communications contributed about 74.1%**, including non-AI applications; an AI-only revenue percentage is not established. Losing orders, adverse pricing or payment terms, or a broad infrastructure slowdown could therefore impair both demand and returns on specialized capacity. Concentration creates potential bargaining leverage; the filing does not establish the customers' actual pricing power or contract protections.

[Evidence: FY2026 filing, consolidated statements and segment/customer disclosures]({COHR_FILING}). Core EBIT of $901.522m removes separately identified restructuring, held-for-sale impairment and the business-sale gain from reported operating EBIT of $897.861m. Ordinary D&A and SBC remain expenses; removing restructuring does not prove it never recurs.

**Operating assumptions owned by the analyst.** Nicolas reaffirmed revenue growth of 35/25/18/12/8%, gross margin of 39/40/41/41.5/42%, and cash PP&E capex of 14/12/10/8/7% of revenue. The story is an initial capacity-supported acceleration, then growth moderation and improved manufacturing efficiency. Dollar capex remains approximately $1.2–$1.4bn annually. Capacity utilization and order conversion must support the falling investment intensity; AGI and AI-driven labor savings are unquantified upside hypotheses.

| Case | Causal operating / valuation conditions | Value/share |
|---|---|---:|
| Low | Growth −5 pp; margin −2 pp; capex −1 pp; WACC 13%; g 2% | ${r['scenarios'][0]['per_share']:.0f} |
| Base | Supported operating paths; WACC 11.8%; g 3% | ${v['per_share']:.0f} |
| High | Growth +5 pp; margin +2 pp; capex −0.5 pp; inventory −15 days; WACC 10%; g 3.5% | ${r['scenarios'][2]['per_share']:.0f} |

**What carries value.** WACC is calculated near {w['calculated_wacc']:.2%}, rounded to 11.8%: nominal 10-year Treasury 5.00% (Sep 15), implied ERP 4.14% (Sep 1), judgment beta 1.75, debt cost 5.5%, tax 20%, and dated capital weights. Nicolas supports above-market risk because concentrated demand and capacity investment can amplify losses and refinancing/dilution needs; this does not measure beta at exactly 1.75. Terminal PV is **{v['terminal_share']:.1%} of EV**. Terminal reinvestment switches to g times closing operating capital; alternative terminal returns of 8/12/16% produce base-forecast values near ${r['terminal_roic_stress'][0]['per_share']:.0f}/${r['terminal_roic_stress'][1]['per_share']:.0f}/${r['terminal_roic_stress'][2]['per_share']:.0f}. At fixed explicit cash flows, WACC, g and bridge, the market price requires terminal FCFF about **{v['reverse_dcf']['multiple_of_base_terminal_fcff']:.1f}×** the modeled terminal amount. That is one implied condition, not proof of market error. [Treasury]({TREASURY}); [ERP]({ERP_SOURCE}).

**Why methods differ.** FN is the only usable verified business-policy peer with positive reported P/E: optical contract manufacturing differs from COHR's owned products, R&D and margins. References are approximately ${p['single_peer_references_per_share']['ev_sales']:.0f} from EV/sales, ${p['single_peer_references_per_share']['reported_pe']:.0f} from reported P/E, and ${p['single_peer_references_per_share']['reported_ev_ebitda']:.0f} from reported EV/EBITDA. Higher COHR EBITDA margin makes the EBITDA reference exceed the sales reference; historical P/E is affected by unusual earnings and share-basis changes. No mechanical average or transaction multiple is adopted. [FN filing]({FN_FILING}).

**Limits and reversal conditions.** June cash/debt/NCI and August actual shares proxy September balances; diluted EPS shares are not substituted for current shares. The bridge retains $300m operating cash, excludes restricted cash, and deducts gross debt, finance leases, $49m pension deficits and NCI. The first cash flow is a remaining-year stub. Debt-note maturity conflicts, springing covenants and intrayear liquidity limit the annual funding model. The separately constrained August subsidiary facility is excluded. A sticky-capex downside fails model funding checks; the low case needs investment restraint. Monitor quarterly GAAP margin, inventory conversion, capex/utilization, customer concentration and a reconciled refinancing schedule. Reconsider initiation after two consecutive reporting dates show improving trailing-year CFO less PP&E capex, supported by capacity utilization and a refreshed valuation offering at least a 25% margin of safety; a lower price alone is insufficient. Withdraw the watch thesis if orders, margins or funding deteriorate; revise upward if durable orders and cash returns demonstrably support higher value.

**AI and validation:** OpenAI Codex assisted research checks, integration and drafting. Nicolas reviewed the memo and requested the risk emphasis above. The complete disclosure, original-record qualifications and material checks are in **Validation-and-AI-Use.pdf** / `docs/validation-and-ai-use.md`.
'''
    (docs/'decision-memo.md').write_text(memo)

    evolution=f'''# Project 1 — Edition B research evolution

**REVIEW DRAFT.** Final preparation date: October 19, 2026. Final valuation and information cutoff: September 15, 2026. Intended user: buy-side committee with no current COHR position.

## Baseline status and unchanged preservation

Nicolas believes `Project_1_Edition_A_Coherent_2026-09-01.md` was the lab checkout submission, but the exact submitted file and separate designated checkpoint receipt are not verified. He is uncertain about AI involvement in that Markdown. The original Markdown is preserved unchanged; its PDF conversion is formatting performed during final preparation, not a historical receipt or an AI-free authorship attestation. The separate `Project 1 Edition A.pdf` is preserved but is not substituted as the official baseline.

The final Research-Evolution.pdf will present the faithful conversion of the **presumed** submitted Markdown first, followed by a dated qualification/addendum and this Edition B. The comparison below is to that preserved document; it does not certify a qualifying Edition A checkpoint. The full statement is in the single validation/AI-use record.

## Current position and consequential check

The proposed position remains **watch/defer** at the saved September 15 price of $271.17. The integrated, signed-FCFF DCF produces a passing-case range of **{draft_range}/share**, base near ${v['per_share']:.0f}, subject to forecast, terminal and funding conditions. The conclusion is proposed for Nicolas's final review. The original operating growth, margin and capex paths have been explicitly reaffirmed by him.

A consequential check independently derives FCFF both from operating NOPAT and from CFO after removing financing tax effects. The two agree in all five forecast years; negative cash flows remain in value. The published instructor training case also reconciles in all twelve outputs. This establishes arithmetic/definition consistency, not proof that forecasts are true.

| Item | Preserved presumed Edition A | Edition B proposal | Primary driver | Evidence / test |
|---|---|---|---|---|
| Thesis / action | Watch/defer; attractive valuation not established | No material action change proposed; maintain watch with quantified conditional range | Own judgment + research + AI-assisted implementation | DCF causal cases, reverse terminal expectation, peer cross-checks; final student review pending |
| Data / date | September 1 valuation date; FY2026 filing; market value unresolved | September 15 valuation and cutoff selected by Nicolas; financial/share dates disclosed | Own decision + source checks | Historical price research, filing statement/cover locators, dated Treasury and ERP |
| Model design | Planned normalization, cases and enterprise-equity bridge | Linked five-year statements feed signed FCFF DCF; minority, finance-lease and pension claims included; common shares explicitly distinguished from EPS shares | Course instruction + own choices + AI-assisted development | Articulation, historical cash reconciliation, independent FCFF identity, bridge and training-case tests |
| Assumptions | Growth durability, investment returns and normalization uncertain | Student-supported operating paths; proposed WACC 11.8% and explicit terminal reinvestment transition; bounded sensitivities | Own judgment + lab discussion + AI-assisted challenge | Assumption-challenge record; full/half range analysis; terminal-return stress |
| Risk / uncertainty | Inventory, capex, customer concentration and cash conversion | Those risks persist; terminal dominance, funding-policy dependence, debt-source inconsistency, baseline and AI-boundary provenance are now explicit | Own analysis + source checks + AI-assisted audit | Filing debt narrative/table comparison, failed funding stress, unchanged historical records |

## Checked AI contribution

The older AI-assisted lab valuation omitted negative FCFE by an explicitly disclosed lab convention; it is unsuitable for this project's required FCFF architecture. The final integration corrects the contribution by retaining signed FCFF and discounting it at WACC, with a complete common-equity bridge. An independent operating-versus-CFO identity, official training answers, and deliberate funding failure tests check the implementation. Disposition in development: **corrected for Project 1**, with student review of the final engine still required. This does not retroactively invalidate the lab's stated exercise convention.

For the historical changed-input exercise, Nicolas reports an unaided original prediction and AI-off test, followed by an AI plausibility check that did not change his prediction. The original plan/results commits corroborate sequencing; separate summaries disclose AI assistance with a sensitivity extension. The complete provenance qualification stays in the single validation record rather than being replaced by an invented clean history.

## What changed from Edition A to Edition B, and why?

The proposed action remains watch/defer, but the justification moves from unresolved valuation to an explicit range and testable cash-conversion conditions. The operating assumptions now flow through linked statements into signed FCFF, and the equity bridge, terminal transition and model failure conditions are visible. Changes reflect course requirements, Nicolas's selected operating thesis, peer discussion and AI-assisted implementation checked against sources and independent calculations. No change is claimed merely to demonstrate evolution; the original checkpoint/authorship uncertainty remains disclosed.
'''
    (docs/'research-evolution.md').write_text(evolution)

    source_rows=[]
    for name,value in r['historical'].items():
        if isinstance(value,(int,float)):
            source_rows.append([name,'calculation' if name in ['reported_operating_ebit','normalized_core_ebit'] else 'filing fact',value,'USD millions','FY2026',COHR_FILING,'Consolidated earnings/cash flows; local PDF 98/102–104','Historical reported amounts retained separately from normalization.'])
    for name,value in r['bridge'].items():
        source_rows.append([name,'judgment' if name=='operating_cash_retained' else 'calculation' if name in ['net_claims','excess_cash_and_investments','pension_deficit'] else 'filing fact',value,'USD millions','2026-06-30 proxy at 2026-09-15',COHR_FILING,'Balance sheet/Notes 8,9,11,15','Gross principal/book proxies; source timing and exclusions disclosed.'])
    for name,value,source,asof,basis in [('market_price',271.17,'https://stockanalysis.com/stocks/cohr/history/','2026-09-15','Historical close; retained from prior research'),('actual_common_shares',195.832246,COHR_FILING,'2026-08-10','Actual common shares, millions; not diluted EPS average'),('risk_free',.05,TREASURY,'2026-09-15','Nominal 10-year Treasury'),('erp',.0414,ERP_SOURCE,'2026-09-01','Monthly adjusted-payout implied ERP')]:
        source_rows.append([name,'source fact',value,'USD/share' if name=='market_price' else 'million shares' if name=='actual_common_shares' else 'decimal rate',asof,source,basis,'Retrieved during final preparation; later data excluded.'])
    for key,value in r['assumptions'].items():
        source_rows.append([key,'forecast / modeling convention',json.dumps(value),'model units; ratios decimal','FY2027–FY2031','docs/assumption-challenge-record.md','Original lab path or disclosed integration convention','Judgments are not company guidance; value/basis/challenge/reversal evidence in linked record.'])
    with (docs/'evidence-ledger.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['item','classification','value','unit','period_or_as_of','source','locator_or_basis','qualification']);writer.writerows(source_rows)
    print('Created review drafts: decision-memo.md, research-evolution.md, evidence-ledger.csv')


if __name__=='__main__':main()
