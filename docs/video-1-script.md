# Video 1 — research evolution and AI-output check

Target 2:40–2:50, maximum 3:00. Preparation script, not an actual transcript. Read only the quoted SAY text. Use your own phrasing and retain only statements that reflect your judgment. The saved documents still label portions as review drafts; reviewing them is necessary before presenting their conclusions as your own.

## Before recording

Open the repository in your code editor with line numbers and readable text. Open these tabs:

1. `docs/sources/edition-a-presumed-original.md`
2. `docs/research-evolution.md`
3. `Pro-Forma Financial Statements/proforma.COHR.py`
4. `project1/engine.py`
5. `project1/test_engine.py`
6. `outputs/project1-base.md`

Keep `docs/validation-and-ai-use.md` available as the supporting disclosure; you do not need to read it aloud or open it during the timed sequence.

Open the integrated terminal at the repository root. Have this command ready to paste:

```sh
python3 project1/test_engine.py FinanceTests.test_known_answer_annuity_and_negative_cash FinanceTests.test_official_course_training_answers
```

Record your screen, clear microphone audio, and small webcam. In VS Code on Mac, use Control+G to jump to a line. No browser interface is needed.

## 0:00–0:35 — Edition A and the original decision

OPEN / SHOW: `docs/sources/edition-a-presumed-original.md`, beginning of file.

POINT TO: “Valuation date” and “Initial thesis: Watch / defer.”

SAY:

“Edition A recommended watch or defer because strong reported growth had not established attractive valuation, especially with weak cash conversion and heavy investment.

“This is the preserved presumed Edition A. I cannot verify the exact submitted checkpoint file or receipt, and its original AI involvement is uncertain. That limitation is disclosed.”

## 0:35–1:10 — Edition B, authorship, and the consequential change

SHOW: `docs/research-evolution.md`, lines 11–15. Keep the change table below the main viewing area rather than reading it.

POINT TO: watch/defer and the $45–$154 range.

SAY:

“Edition B keeps watch or defer, but replaces unresolved valuation with a conditional range of about 45 to 154 dollars per share.

“The change came from a mixture: course requirements shaped the valuation framework; I selected the September 15 date and reaffirmed the operating paths; Codex assisted implementation and checks. I discussed growth and margins with Zachary, but I cannot attribute a specific undocumented challenge to him.”

## 1:10–1:45 — show the AI-assisted result and its correction

SHOW: `Pro-Forma Financial Statements/proforma.COHR.py`, lines 220–232.

POINT TO: `max(0, x["fcfe"])` at line 225.

SAY:

“One AI-assisted result that needed correction for this project was the older lab valuation. This expression omitted negative free cash flow to equity under the lab’s stated convention. Carrying that treatment into this project would omit cash outflows.”

SHOW: `project1/engine.py`, lines 117–124.

POINT TO: `row['fcff']`, `via_cfo`, and `fcff_identity_gap`.

SAY:

“The disposition was corrected for this project: use signed free cash flow to the firm, discount at WACC, and reconcile operating cash flow with a separate derivation.”

## 1:45–2:20 — demonstrate the check and explain why it is sufficient

SHOW: `project1/test_engine.py`, lines 25–30.

POINT TO: the negative first cash flow at line 29 and the expected value reduction at line 30.

SAY:

“This test changes the first cash flow from positive 100 to negative 100. Value must fall by 200 discounted one year. A second test compares the valuation function with published course answers.”

SHOW: Terminal. Paste and run the prepared command. Pause on `Ran 2 tests` and `OK`.

SAY:

“Both pass. These checks are sufficient to support the cash-flow treatment and arithmetic. They do not establish that the forecast will occur.”

## 2:20–2:45 — decision and remaining uncertainty

SHOW: `outputs/project1-base.md`, lines 6–17.

POINT TO: negative FY2027 FCFF of -435.467 on line 13, then terminal share of 87.40% on line 9.

SAY:

“The output retains about 435 million dollars of negative first-year cash flow. But terminal value still represents 87.4 percent of enterprise value.

“My decision remains watch or defer. What changed is the justification: cash conversion, funding, and terminal assumptions are now explicit and testable, rather than unresolved research questions.”

## Rehearsal and timing

Aim to finish by 2:45. The actual duration depends on your speaking pace and navigation; rehearse once. If you approach 3:00, shorten the partner-discussion sentence and the final paragraph, while retaining the authorship disclosure, visible AI-assisted result, correction, performed check, and explanation of what the evidence establishes.

This video is about the research decisions and the treatment of AI output. Avoid extending it into the architecture walkthrough from Video 2. Save the actual corrected transcript after recording; do not label this script a transcript.
