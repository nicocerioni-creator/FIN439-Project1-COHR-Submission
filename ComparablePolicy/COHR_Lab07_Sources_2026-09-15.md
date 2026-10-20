# COHR Lab 07 input and source record

Comparison date: September 15, 2026. Prepared September 17, 2026. The calculator was executed on user instruction; exit code 0. Full output: COHR_Lab07_Output_2026-09-15.txt.

## Initial policy — unchanged

Mandatory requirements: operations on more than one continent; at least 50% of revenue from datacenter and/or communications (no double counting); market capitalization at least USD 5 billion on the comparison date. Supporting similarities: optical products, manufacturing/R&D/inventory investment, and datacenter/network demand. Some supporting similarities suffice; a failed mandatory requirement excludes a candidate. An unresolved requirement is not a verified pass.

## Input/source table

All prices refer to September 15, 2026, regular-session closing prices in USD. All EPS figures below are annual reported GAAP diluted EPS in USD per listed common/ordinary share, not quarterly, forecast or adjusted EPS.

| Company | Decision / calculator treatment | Closing price | Annual GAAP diluted EPS | Fiscal year-end | Annual earnings publication date | Price source locator | Earnings source locator |
|---|---|---:|---:|---|---|---|---|
| Coherent (COHR) | Target; entered | 271.17 | 4.12 | 2026-06-30 | 2026-08-12 | [Investing.com history](https://www.investing.com/equities/coherent-historical-data), Sep 15, 2026 row, Price column | [Company annual release](https://ir.coherent.com/news-releases/news-release-details/coherent-corp-reports-fourth-quarter-and-full-year-fiscal-2026), Table 1, GAAP Financial Results, FY2026 column, Diluted Earnings (Loss) Per Share; [SEC 10-K](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm), Item 8, Note 19, Earnings Per Share, printed p. 85 |
| Fabrinet (FN) | Qualify; only numerically usable peer | 374.91 | 13.05 | 2026-06-26 | 2026-08-17 | [Investing.com history](https://www.investing.com/equities/fabrinet-historical-data), Sep 15, 2026 row, Price column | [Company annual release](https://investor.fabrinet.com/node/13666), Fiscal Year 2026 Financial Highlights — GAAP Results; [SEC 10-K](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/fn-20260626.htm), Item 8, Note 5, Earnings per ordinary share, printed p. 74, FY2026 diluted row |
| Lumentum (LITE) | Qualify as business candidate; EXCLUDE from usable multiples because annual diluted EPS is negative; entered for diagnostics only | 838.96 | -92.96 | 2026-06-27 | 2026-08-11 | [Investing.com history](https://www.investing.com/equities/lumentum-holdings-inc-historical-data), Sep 15, 2026 row, Price column | [Company annual release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx), Full Fiscal Year 2026; [SEC 10-K](https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm), Item 8, Note 3, Earnings Per Share, printed p. 83 |

All three annual releases predate the valuation date. Publication date means the annual earnings release date, not the fiscal year-end or 10-K filing date. Fabrinet and Lumentum use 52/53-week fiscal years; COHR uses June 30. These are full fiscal years, not identical calendar windows.

## Business decisions and remaining checks

- FN: Qualify because optical production, capacity utilization, and network/datacenter demand are relevant to COHR. Its contract-manufacturing model requires a caveat about product ownership, R&D and margins. FY2026 datacenter revenue 47.9% plus communications infrastructure 33.3% = 81.2%; facilities in Asia and the United States support the geography criterion. Sources: FN 10-K Item 1 Business; Item 2 Properties; Item 7 Results of Operations, Revenues (printed p. 45). Exact September 15 market capitalization remains unresolved; the calculator input is prepared under the user's qualify decision, not a claim that all policy checks are complete.
- LITE: Business similarities are optical transceivers/components, AI/cloud network demand, and manufacturing-capacity investment. Sources: LITE 10-K Item 1 Offerings (p. 5) and Industry Conditions (p. 3). Annual reported EPS is negative, so no meaningful reported annual P/E is used. The annual release attributes the loss chiefly to a noncash debt-extinguishment charge. The >=50% revenue test and exact September 15 market capitalization remain unresolved. Retained in PEERS for diagnostics at the user's request; negative EPS prevents inclusion in the usable multiples.

## Price-source and share-basis checks

- Started at Nasdaq Historical Quotes: [COHR](https://www.nasdaq.com/market-activity/stocks/cohr/historical), [FN](https://www.nasdaq.com/market-activity/stocks/fn/historical), [LITE](https://www.nasdaq.com/market-activity/stocks/lite/historical). Those pages returned no usable historical rows. Prices above therefore use the named secondary provider Investing.com, not a claimed Nasdaq verification.
- COHR's opened Investing.com September 15 row shows 271.17, agreeing with the prior DCF input and the indexed [FinanceCharts history](https://www.financecharts.com/stocks/COHR/summary/price). A search snippet initially showed 270.46; the directly opened date row showed 271.17. This retrieval discrepancy is retained rather than silently omitted. FinanceCharts direct opening presented a CAPTCHA, so it was only supplementary indexed evidence.
- COHR and FN are USD-quoted common/ordinary shares, not ADRs; their annual EPS is also in USD. The financial statements label dollar amounts in thousands or millions but expressly exclude per-share data: do not scale the EPS figures by 1,000 or 1,000,000.
- [COHR Stock Analysis statistics](https://stockanalysis.com/stocks/cohr/statistics/), Stock Splits, reports the last split as June 27, 2011; [FN statistics](https://stockanalysis.com/stocks/fn/statistics/), Stock Splits, reports no recorded split. These secondary checks identify no intervening split requiring adjustment between FY2026 earnings and the comparison date. No currency, ADR-ratio, or split adjustment has been applied to the entered COHR/FN pairs.
- The historical prices are taken from the Price/closing-price column, not a total-return or dividend-adjusted series. LITE's price is printed in the input audit; its negative EPS causes rejection before any multiple or implied valuation is calculated.

## Reported versus adjusted earnings

Only reported annual GAAP diluted EPS is entered into the calculator. Non-GAAP/adjusted EPS, quarterly EPS and guidance are excluded from its inputs. No adjustment is made to remove COHR's business-sale gain or LITE's debt-extinguishment loss. Company releases separately present non-GAAP reconciliations; those are not substituted here.

## Execution and recorded result

Executed `python3 ComparablePolicy/ComparablePolicy_2026-09-15_Lab07.py` from the repository root, with output redirected to `ComparablePolicy/COHR_Lab07_Output_2026-09-15.txt`. Exit code: 0.

The user requested COHR, FN and LITE inputs in this run. LITE was added for visible diagnostics, without changing the business policy or allowing a negative multiple into the valuation. No adjusted earnings or alternative valuation method was substituted.

- COHR input: price 271.17; annual reported diluted EPS 4.12. Target P/E: 65.817961x.
- FN input: price 374.91; annual reported diluted EPS 13.05. Peer P/E: 28.728736x.
- COHR single-peer reference: (374.91 / 13.05) * 4.12 = **USD 118.36 per share**, rounded only for display.
- LITE input: price 838.96; annual reported diluted EPS -92.96. Rejected from usable multiples. Zero EPS makes division undefined; negative EPS represents a loss rather than a positive earnings base for a meaningful P/E valuation.
- Only one usable peer: **no implied peer range**. Removing FN leaves no estimate; removing LITE changes the reference by USD 0.00 because LITE was already excluded.
- This is a conditional single-peer reference, not a fully verified policy-compliant peer range. Exact date-matched market-cap evidence remains a documented limitation.

## Follow-up investigation of unresolved evidence

- A targeted dated-market-cap search located [FinanceCharts FN market-cap history](https://www.financecharts.com/stocks/FN/summary/market-cap), whose indexed September 15, 2026 row reports USD 13.435 billion and approximately 35.835 million shares. This secondary evidence supports being above the USD 5 billion threshold; exact contemporaneous shares and primary/exchange confirmation remain unresolved. Nasdaq historical pages previously returned unavailable data. Missing evidence: a reliable date-matched market-cap record or the September 15 closing price paired with a verified applicable share count.
- Reopened both FY2026 SEC 10-Ks before running. FN's Item 1, Item 2 and Item 7 support optical manufacturing, operations across continents and 81.2% combined qualifying revenue. Its contract-manufacturing model remains the stated caveat.
- LITE's Item 1 supports optical products and AI/network demand; its FY2026 reporting uses one segment and Components/Systems categories including industrial products. A further revenue-mix search did not establish a FY2026 datacenter/communications percentage. Missing evidence: an annual end-market revenue reconciliation separating qualifying datacenter/communications from consumer/industrial sales. Older segment percentages or one quarter would not establish that annual figure. Exact comparison-date market cap remains unresolved as well; neither gap overrides the independently verified negative-EPS exclusion.

No Asbury, AutoNation or Group 1 inputs are used in this run. The prior case remains in Git history.
