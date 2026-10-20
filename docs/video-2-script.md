# Video 2 — 4:15 recording script

Preparation script, not an actual transcript. Target: 4:00–4:30, including navigation. Read only the quoted SAY paragraphs. Rehearse once with a timer; the timestamps are pacing targets.

## Before recording

- Open the submitted COHR-DCF-Analysis repository in your code editor.
- Enable line numbers, enlarge text, and close unrelated tabs.
- Open these five tabs in order: `project1/app.py`, `project1/engine.py`, `project1/research.py`, `project1/test_engine.py`, `outputs/cold-run-20261020T022118Z.txt`.
- Open an integrated terminal at the repository root. Run `pwd` before recording to confirm the folder ends in `COHR-DCF-Analysis`.
- Have this command ready to paste during the validation section:

```sh
python3 project1/test_engine.py FinanceTests.test_real_funding_failure_and_bad_input_rejected
```

- Share your editor with a small webcam tile and clear microphone audio. Keep the webcam away from the code. You do not need the browser interface.
- In VS Code on Mac, Control+G opens Go to Line. Navigate directly instead of scrolling through entire files. Keep the script on another screen or device.

## 0:00–0:35 — architecture and data flow

OPEN / SHOW: `project1/app.py`, lines 97–109.

POINT TO: `run(controls)` on line 105.

SAY:

“This is the code behind my Coherent valuation application. Codex assisted with implementation and testing. The interface sends driver inputs to the engine through this run function, so the displayed valuation comes from the same financial model.”

SHOW: `project1/engine.py`, lines 89–98.

POINT TO: `deepcopy(lab.ASSUMPTIONS)` on line 91, then `lab.project(assumptions=a)` on line 98.

SAY:

“The engine imports the preserved lab model. It copies the assumptions, applies driver changes, and projects the statements. Copying the assumptions prevents a stress case from overwriting the base.”

## 0:35–1:20 — financial logic and reconciliation

SHOW: `engine.py`, lines 117–129.

POINT TO: FCFF formula at lines 117–119, then `via_cfo` at 121–123, then `fcff_identity_gap` at 124.

SAY:

“Free cash flow to the firm starts with after-tax operating income, adds back noncash charges, and subtracts working-capital investment, capital spending, and intangible purchases. Negative cash flows remain negative and reduce value.

“A separate calculation starts from operating cash flow and removes financing effects using after-tax interest and a debt-cost tax adjustment. The two calculations must agree under the model’s current tax conventions.

“The check loop also tests statement reconciliation, the cash floor, and financing limits. Passing these checks establishes internal consistency, not forecast accuracy.”

## 1:20–2:10 — WACC, terminal value, and common equity

SHOW: `project1/research.py`, lines 19–36.

POINT TO: input components on line 20 and WACC calculation on line 26.

SAY:

“The research file separates dated source inputs from judgments. Treasury yield and the equity risk premium are sourced. Beta, borrowing cost, and normalized tax are judgments. These produce a rounded WACC of 11.8 percent.”

SHOW: `engine.py`, lines 130–149.

POINT TO: terminal reinvestment at 134, terminal FCFF at 135, net claims at 144–145, and per-share value at 149.

SAY:

“Terminal growth is 3 percent. Terminal cash flow deducts reinvestment calculated as growth times closing operating capital. The discount function values this cash flow using WACC minus growth and discounts it back.

“The equity bridge deducts debt, minority interests, finance leases, and pension deficits, and adds excess cash and investments. It retains 300 million dollars of operating cash. Common equity is then divided by actual common shares.”

## 2:10–3:15 — demonstrate the targeted funding test

SHOW: `project1/test_engine.py`, lines 57–63.

POINT TO: `growth_shift_pp:5` at 58, `assertFalse` at 59, and `cash_floor_shortfall` at 60.

SAY:

“A high-risk claim is that the projected growth can be financed. This test increases growth by five percentage points in every forecast year while holding other driver inputs constant. Faster growth requires inventory and capacity spending before cash is recovered.

“The test expects the scenario to fail its overall checks and specifically requires a cash-floor shortfall. This prevents a conditional valuation from being treated as a fundable investment case.”

SHOW: Integrated terminal. Paste and execute:

```sh
python3 project1/test_engine.py FinanceTests.test_real_funding_failure_and_bad_input_rejected
```

POINT TO: the named test, `Ran 1 test`, and `OK`. Pause briefly so the result is readable.

SAY:

“The test passes because it detects the expected financial failure. It also checks rejection of invalid inputs and terminal growth equal to WACC. These are AI-assisted integration tests, separate from my historical changed-input exercise.”

## 3:15–3:45 — reproduction and saved evidence

SHOW: `outputs/cold-run-20261020T022118Z.txt`. Show the six passing tests and the base output, then jump to `FINAL STATUS: PASS` at the bottom.

POINT TO: `Ran 6 tests`, `$75.60`, and `FINAL STATUS: PASS`.

SAY:

“To reproduce from the repository root, run python3 project1 slash test underscore engine dot py, then python3 project1 slash engine dot py. The engine regenerates the saved model output.

“The clean-run log records a fresh copy and virtual environment using only the standard library. All six tests passed, and the base output was 75 dollars and 60 cents per share.”

## 3:45–4:15 — limitation and close

SHOW: `engine.py`, lines 40–50.

POINT TO: dated balance-sheet proxies on line 42, terminal reinvestment on 45, and funding limitations on 48.

SAY:

“The largest valuation risk is terminal dependence: about 87.4 percent of base enterprise value comes from terminal value. The terminal reinvestment transition therefore matters substantially.

“Cash, debt, and shares also use disclosed dated proxies, while funding checks simplify maturity timing and covenants. Passing tests supports consistency and reproducibility. It does not prove the operating forecast or eliminate financing risk.”

## Timing and ownership check

The narration is about 475 words. At roughly 130 words per minute, allow about 35 seconds for navigation, the test, and pauses to finish near 4:15. Your rehearsal determines the actual duration.

If you exceed 4:30, omit the sentence about invalid inputs and the sentence about dated proxies. Keep the targeted test, the explanation of its passing result, reproduction commands, and terminal dependence.

Before recording, make sure you can explain why assumptions are copied, why after-tax interest is added back when deriving FCFF from CFO, and why a financial scenario failure can produce a passing test. Use your own phrasing where it helps you explain naturally. Save an actual corrected transcript after recording; do not submit this preparation script as a transcript.
