# COHR provisional integrated FCFF output

Valuation date and information cutoff: 2026-09-15.
Generated during AI-assisted final preparation; not an AI-closed run or a historical submission receipt.

Base diagnostic: $75.60 per actual common share; WACC 11.8%, g 3% (judgment-dependent).
Enterprise value: $16,773.762m; common equity: $14,805.360m.
Net claims: $1,968.402m; shares: 195.832246m.
Terminal PV / EV: 87.40%. Checks: PASS.

| Fiscal year | Revenue | EBIT | CFO | PP&E capex | Signed FCFF | Closing cash |
|---|---:|---:|---:|---:|---:|---:|
| 2027 | 9,609.544 | 1,362.633 | 773.731 | 1,345.336 | -435.467 | 575.323 |
| 2028 | 12,011.930 | 1,873.861 | 1,306.634 | 1,441.432 | 0.935 | 398.976 |
| 2029 | 14,174.078 | 2,418.098 | 1,931.228 | 1,417.408 | 647.912 | 811.993 |
| 2030 | 15,874.967 | 2,826.538 | 2,458.031 | 1,269.997 | 1,313.585 | 300.000 |
| 2031 | 17,144.965 | 3,182.105 | 3,008.008 | 1,200.148 | 1,863.187 | 671.977 |

## Causal scenarios

| Scenario | Conditional value / share | Funding/articulation |
|---|---:|---|
| Low: demand slowdown with investment restraint | $44.79 | PASS |
| Base: growth fades and manufacturing improves | $75.60 | PASS |
| High: stronger demand plus execution and cash discipline | $153.75 | PASS |
| Stress: slowdown with sticky investment (not executable) | $40.63 | FAIL; excluded |

Passing-case DCF range: $45–$154/share; a scenario range, not a confidence interval.

## Single-peer cross-checks

- reported_pe: $118.36/share (qualified single-peer reference).
- ev_sales: $89.85/share (qualified single-peer reference).
- reported_ev_ebitda: $164.02/share (qualified single-peer reference).

Full inputs, all three statements, checks, bridge, WACC–growth grid, reverse DCF, and one-at-a-time sensitivities are visible in `project1-base.json`.

## Limitations

- WACC build uses September 15 Treasury 5.00%, September 1 ERP 4.14%, and judgment beta 1.75 / debt cost 5.5% / tax 20%; beta is not a regression estimate. Rounded base WACC is 11.8%.
- June 30 cash, debt and NCI and August 10 common shares are proxies at September 15; no actual interim balance sheet is asserted.
- Actual common shares are used, not historical diluted EPS weighted-average shares. SBC is retained as an economic expense without a cash add-back or forecast share issuance.
- FY2027 DCF uses a 288/365 remaining-year fraction under uniform cash generation; annual statements still show the full fiscal year. Seasonality and interim actual cash flows are not modeled.
- Terminal reinvestment changes to g times closing modeled operating capital; this transition is an assumption, not company guidance.
- Financing failures are shown separately from operating value: conditional DCF diagnostics do not make an unfunded scenario executable.
- No new acquisitions, divestitures, refinancing, NCI earnings/distributions or incremental capacity constraints beyond the inherited lab conventions.
- Debt maturity table conflicts with some narrative maturity dates; annual funding results follow the table and are conditional. Springing maturities, intrayear timing and covenants are not modeled.
- The August 2026 ~$945m subsidiary facility was known before the cutoff but is excluded from parent funding capacity because its uses/guarantees are restricted. Funding failures are not company insolvency forecasts.
- Gross debt and NCI book value proxy market claims; finance leases and $49m pension deficits are deducted separately. Operating lease costs remain expenses; strategic equity assets receive no separate value without a verified realizable amount.
