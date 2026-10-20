# Own-pro-forma sensitivity interpretation

Valuation date: September 15, 2026. FY2031 EBIT and signed FCFF are USD millions; value is USD per actual common share. Generated from the integrated engine, not the older FCFE exercise.

Each endpoint changes only one independent driver from the same restored base. Valid spans include the base and all passing endpoints; funding-invalid endpoints are excluded. The excluded diagnostics remain visible in the full output. Spans are sensitivity measures, not probabilities or confidence intervals.

| Driver | Range scale | Passing endpoints | EBIT span ($m) | FCFF span ($m) | Value span ($/share) |
|---|---:|---|---:|---:|---:|
| growth_shift_pp | 1.0 | low + base | 615.429 | 57.258 | 14.004 |
| margin_shift_pp | 1.0 | high + base | 233.172 | 201.272 | 10.024 |
| capex_shift_pp | 1.0 | low + base | 0.000 | 267.947 | 5.492 |
| inventory_shift_days | 1.0 | low + base | 0.000 | 54.018 | 3.845 |
| wacc_pct | 1.0 | low, high + base | 0.000 | 0.000 | 63.201 |
| terminal_growth_pct | 1.0 | low, high + base | 0.000 | 0.000 | 9.317 |
| growth_shift_pp | 0.5 | low + base | 320.910 | 25.352 | 7.303 |
| margin_shift_pp | 0.5 | high + base | 116.586 | 100.636 | 5.012 |
| capex_shift_pp | 0.5 | low + base | 0.000 | 133.974 | 2.746 |
| inventory_shift_days | 0.5 | low + base | 0.000 | 27.009 | 1.923 |
| wacc_pct | 0.5 | low, high + base | 0.000 | 0.000 | 27.144 |
| terminal_growth_pct | 0.5 | low, high + base | 0.000 | 0.000 | 4.613 |

Revenue growth is the main FY2031 EBIT driver among these tests. Sales compound across five years; holding gross margin, SG&A/gross-profit and R&D/revenue fixed transmits a larger revenue base into operating profit. Margin also changes EBIT, but its tested range is smaller in its resulting dollar effect.

Capex intensity is the main FY2031 FCFF driver over these passing-case ranges. Cash investment is deducted directly from operating FCFF. Lower capex also produces less accumulated PP&E and depreciation add-back; the net investment effect dominates here. Gross margin ranks next: it raises NOPAT and, under the COGS-based rule, reduces inventory requirements. Growth consumes inventory and capex as well as generating profit, so its free-cash-flow effect is much smaller than its EBIT effect.

WACC is the largest value driver over these ranges because terminal PV is about 87.4% of base enterprise value. Among operating drivers, growth has the largest passing-case value span, followed by margin. A smaller spread between WACC and terminal growth increases terminal value; it does not improve operating cash generation.

Range dependence is visible: with the full ranges, the passing-case FCFF growth span (about 57.258m) slightly exceeds the inventory-day span (about 54.018m). At half ranges, inventory days (about 27.009m) exceeds growth (about 25.352m). Growth remains the leading EBIT driver, capex the leading FCFF driver, and WACC the leading value driver. The full value ordering is unchanged at half range. This is evidence against claiming a universal ranking.

The old lab identified gross margin as the main signed-FCFE driver across its valid cases. That is a different output, includes borrowing/repayment, and tested only growth and margin. The integrated FCFF comparison adds capex, inventory, WACC and terminal growth and excludes financing cash flows; the two rankings are not interchangeable.

Accounting limitation: capex/inventory tests hold operating margins fixed, so they do not separately forecast price, volume, capacity utilization or incremental D&A expenses through EBIT. D&A is already in the targeted GAAP margins; these tests do not deduct it twice. They are controlled sensitivities, not complete business scenarios. The causal low/high cases combine operating and investment responses separately.

Input ranges: growth ±5 pp/year; margin ±2 pp/year; capex intensity ±2 pp/year; ending inventory ±30 days; WACC 9–13% around base 11.8%; g 2–4% around 3%. Half ranges halve each distance from its base. These unequal ranges and asymmetric valid endpoints must accompany any ranking.
