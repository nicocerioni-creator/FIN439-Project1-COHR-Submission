# Project 1 integration audit

Reviewed October 19, 2026 with OpenAI Codex. This is an integration audit, not a completed investment recommendation.

## Existing work that can be reused

- `Pro-Forma Financial Statements/proforma.COHR.py`: five-year statements and opening balance-sheet reconstruction. Re-executed with `--self-test`: exit 0; all five years articulate and the base financing checks pass.
- `Proforma Financial Analysis/test_cohr_sensitivity.py`: five tests re-executed successfully. Tests cover input isolation, restoration, accounting/nonfinite failures, and exclusion of funding-invalid runs from spans.
- Existing sensitivity results and locked prediction record: preserve unchanged. Their existence does not establish an AI-off prediction or AI-off execution. Historical context explicitly describes AI assistance with preparation; exact compliance remains to be established by the student.
- Existing source map and local FY2024–FY2026 filings. The FY2026 SEC HTML was independently opened during this audit and corroborates revenue, restructuring/impairment/gain amounts, NCI, and August 10 common shares.
- Existing peer policy and reported-GAAP P/E analysis. FN is a conditional single-peer reference, not a peer valuation range. The documented policy gaps remain limitations.

## Required integration and corrections

1. Replace the disconnected manually entered DCF cash-flow path with FCFF calculated from the pro-forma. Preserve all signed cash flows; do not use the lab's positive-only FCFE valuation as the final project valuation.
2. Nicolas selected September 15, 2026 as the final valuation date and information cutoff on October 19, 2026. Explain FY2026 opening balances versus later market evidence. June 30 with subsequently released information is not a contemporaneous June 30 recommendation. Original Edition A retains its original date unchanged.
3. Support WACC with dated components. The old DCF explicitly calls 10% a placeholder; the pro-forma's 11% is a judgment, not a verified CAPM estimate. Do not silently relabel either as sourced.
4. Complete the bridge with gross debt, excess unrestricted cash/investments, NCI, preferred claims if any, and consistent lease treatment. Keep restricted cash excluded. Resolve operating cash treatment and common-share basis explicitly.
5. Document the terminal transition. The lab changes from explicit investment ratios to growth times closing operating capital; this assumption materially affects value and must be challenged rather than hidden.
6. Add a bounded driver interface, reset, visible diagnostics, causal scenarios, value sensitivities, range-ranking comparison, and reverse DCF using the integrated engine.
7. Complete an enterprise-value peer multiple using consistent dates and definitions. Negative EPS excludes LITE from positive P/E, but does not by itself exclude an economically meaningful EV multiple.
8. Complete historical normalization and the assumption-challenge record. The model uses ending inventory/COGS days, not the historical average-inventory-days convention; label the basis change.
9. Complete training-case reconciliation, independent checks, highest-risk test, fresh-environment cold run, visible executed output, PDFs, README, manifest, and recordings/transcripts.

## Independent accounting derivations

USD millions. Current lab assumptions retained solely for this audit.

FCFF = EBIT × (1 − tax rate) + depreciation + amortization − inventory investment − other operating working-capital investment − cash PP&E capex − intangible purchases.

| Fiscal year | Signed FCFF from pro-forma |
|---|---:|
| 2027 | -435.467188 |
| 2028 | 0.934730 |
| 2029 | 647.911973 |
| 2030 | 1,313.585188 |
| 2031 | 1,863.186660 |

Second derivation: CFO + cash interest × (1 − tax rate) − debt-cost amortization × tax rate − PP&E capex − intangible purchases. This agrees within USD 0.00000001 million in all five years. The debt-cost term removes the financing tax effect retained by the lab's CFO calculation. This identity relies on the current positive pretax-income cases and model tax conventions; it is not a blanket rule for loss cases.

FY2026 reported operating EBIT = pretax income 847.733 + interest 190.267 − other income 140.139 = 897.861.

Core EBIT before separately identified restructuring, held-for-sale impairment, and business-sale gain = revenue 7,118.181 − COGS 4,449.141 − R&D 722.952 − SG&A 1,044.566 = 901.522. Equivalent bridge: 897.861 + 63.390 + 64.404 − 124.133 = 901.522. This is a normalization choice, not proof that restructuring never recurs; stock compensation and ordinary D&A remain expenses.

Gross debt 3,257.482 − unrestricted cash 1,162.018 − short-term investments 825.000 + NCI 334.705 = 1,605.169 net claims. Retaining USD 300 million as operating cash increases the deduction from EV to common equity to 1,905.169. NCI book value and gross debt principal are proxies, not observed market values. No bridge choice has yet been finalized.

## Evidence

- [FY2026 SEC Form 10-K](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm): cover (common shares), consolidated balance sheet, earnings, cash flows, debt note, and EPS note. Local PDF statement pages 96, 98, 102; debt page 122; EPS pages 151–152.
- [FY2026 annual company release](https://ir.coherent.com/news-releases/news-release-details/coherent-corp-reports-fourth-quarter-and-full-year-fiscal-2026), published August 12, 2026. Opened during audit.

All test runs in this audit were AI-assisted preparation, not the required AI-closed changed-input exercise or a fresh-environment cold run.
