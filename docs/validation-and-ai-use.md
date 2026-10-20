# Project 1 — Validation and AI Use

Working record. The completed record will be frozen as Validation-and-AI-Use.pdf for final submission.

## Edition A submission and authorship uncertainty

Disclosure recorded October 19, 2026. Statement reviewed and approved by Nicolas Cerioni.

> I believe the Edition A Markdown file was submitted through a Week 2 or Week 3 lab checkout, but I cannot currently verify the exact submitted file or locate a separate designated Edition A checkpoint receipt. I am also uncertain whether generative AI assisted preparation of that Markdown version. The PDF conversion was created with Codex during final preparation and does not establish the original document’s authorship or submission timing. Both original files have been preserved.

### Files referenced

- Presumed submitted Markdown: `NicolasCerioni/COHR-research/Project_1_Edition_A_Coherent_2026-09-01.md`, relative to the AI Finance 2026 workspace.
- PDF converted from that Markdown during final preparation: `NicolasCerioni/COHR-research/Project_1_Edition_A_Coherent_2026-09-01.pdf`.
- Separate preserved PDF, not verified as the submitted baseline: `NicolasCerioni/COHR-research/Project 1 Edition A.pdf`.

The designated Edition A checkpoint receipt, exact submitted file, and original AI involvement remain unverified. A weekly lab checkout is not treated as proof of the designated checkpoint. This disclosure does not establish that a qualifying Edition A checkpoint exists or attest to AI-free authorship.

## AI assistance during final preparation

- Tool: OpenAI Codex.
- Assistance recorded October 19, 2026: reviewed the supplied project and submission requirements; inventoried local files; converted the Edition A Markdown into a PDF without changing the Markdown; drafted the uncertainty disclosure above, which Nicolas reviewed and approved; created this working record.
- Conversion checks: verified the source prose appeared in order in the converted PDF, confirmed the Markdown was unchanged, and visually reviewed all three PDF pages. These checks address conversion fidelity, not original authorship or checkpoint compliance.
- Nicolas reviewed the decision memo and requested stronger risk emphasis. Codex incorporated capacity-investment return uncertainty, weak positive CFO/negative simple FCF, and potential bargaining leverage from customer concentration. The filing was used to qualify the unsupported AI-only revenue percentage and the claim of extreme pricing power. The resulting memo retains the student's thesis while distinguishing evidence from inference.

## Locked Changed-Input Record — preserved evidence and boundary status

### Student account recorded October 19, 2026

Nicolas states that he made the original sensitivity prediction with AI off, then asked AI for its thoughts. He reports that AI supported the prediction as reasonable and plausible, he retained the original prediction unchanged, and he ran his test with AI off. The AI contribution is therefore disclosed as a subsequent plausibility check, not as the origin of his prediction. He discussed his revenue-growth and gross-margin increases with lab partner **Zachary**. This is his current account, not a newly recovered pre-run document. The exact content of a Zachary-authored challenge has not been preserved in the files inspected so far; no specific challenge is attributed to him without further evidence.

### Corroborating historical files

- Prediction record: `Proforma Financial Analysis/Lab11_Locked_Changed_Input_Record_2026-09-29.md`, originally committed under `Pro-Forma Financial Statements/` in commit `ba18386e049577134ee73e5dfbdca0a0703bb134` at **2026-09-29 17:32:18 -04:00**.
- First sensitivity-extension/results commit: `f027844`, **2026-09-29 17:39:37 -04:00**. The commit ordering corroborates that the preserved plan precedes the preserved results; it does not independently verify the first execution time or absence of AI.
- Results: `Proforma Financial Analysis/COHR_Lab11_Sensitivity_Results.md` and `.json`; restoration and funding failures are retained.
- `Proforma/2026-09-29_Lab11_Completion_Session-Summary.md` in the surrounding workspace documents AI assistance with creating and executing the sensitivity extension. The earlier saved September 29 session summary also describes AI-assisted preparation of the plan and supporting analysis. These summaries do not establish who first originated each prediction, but prevent treating the preserved extension run as independently verified AI-closed evidence.

### Exact changed inputs and preserved results

All paths are FY2027 / FY2028 / FY2029 / FY2030 / FY2031; shifts are absolute percentage points (pp). EBIT and signed FCFE are USD millions.

| Case | Old path (%) | New path (%) | Preserved expected effect | Actual FY2031 EBIT change | Actual FY2031 FCFE change | Funding result |
|---|---|---|---|---:|---:|---|
| Growth lower | 35 / 25 / 18 / 12 / 8 | 30 / 20 / 13 / 7 / 3 | EBIT down about 615; FCFE tentatively up, financing-dependent | -615.429 | +406.768 | Pass |
| Growth higher | 35 / 25 / 18 / 12 / 8 | 40 / 30 / 23 / 17 / 13 | EBIT up about 728; FCFE tentatively down about 100–200 | +727.994 | -204.780 | Fail; diagnostic only |
| Margin lower | 39 / 40 / 41 / 41.5 / 42 | 37 / 38 / 39 / 39.5 / 40 | EBIT down about 233; FCFE down about 200–450 | -233.172 | -433.119 | Fail; diagnostic only |
| Margin higher | 39 / 40 / 41 / 41.5 / 42 | 41 / 42 / 43 / 43.5 / 44 | EBIT up about 233; FCFE up about 200–650 | +233.172 | +665.298 | Pass |

Initial and restored FY2031 base: EBIT **3,182.105** and signed FCFE **371.977**. The results preserve signed annual cash flows. The growth-lower FCFE increase slightly exceeds its tentative upper estimate (+400); the margin-higher increase slightly exceeds its rough upper estimate (+650). The recorded mechanism is reduced earlier revolver use and final-year repayment, which can outweigh the operating-cash-flow effect. Invalid cases are not included in valid-case spans. Restoration agrees across all original inputs and statement fields.

Expected investment-decision effect before execution: **not explicitly preserved in the original locked record**. It is not retroactively supplied as a pre-run prediction. Actual decision effect: the saved sensitivity exercise does not issue an investment action and marks value/share unavailable; it cannot alone establish an initiation decision. Its substantive contribution is identifying financing-sensitive cash flow and invalid cases. This is the explanation for no demonstrated action change, not a claim that a decision was predicted in advance.

### Qualification

Status: **student-declared AI-off prediction and test, with partial corroborating historical evidence**. The preserved commits corroborate a plan-before-results sequence. They do not independently establish the text/timestamp of the original prediction before AI feedback or identify the student's separate AI-off run. The AI-assisted extension documented in session summaries remains disclosed; its execution is not relabeled AI-off. Nicolas's account and the provenance limits are both preserved. The record does not conclude that AI originated his ideas. No file or timestamp has been altered to manufacture a clean historical boundary; the instructor can assess the evidence under the published rule.

## Remaining validation evidence

### Current integration, sources and clean run (supersedes earlier draft numbers)

The earlier USD 86.65 result below is retained as development history and is **superseded**. The current proposed base uses **11.8% WACC**, includes **USD 14.233 million finance leases** and **USD 49 million pension deficits**, and produces approximately **USD 75.60/share**, EV **USD 16,773.762 million**, common equity **USD 14,805.360 million**, net claims **USD 1,968.402 million**, and terminal PV/EV **87.40%**. Consult `outputs/project1-base.json` for full precision. The operating base paths are unchanged and explicitly reaffirmed by Nicolas; WACC and terminal assumptions remain subject to his final review.

- WACC components independently checked: Treasury September 15 nominal 10-year yield **5.00%** (not the real yield); Damodaran September 1 adjusted-payout implied ERP **4.14%**, excluding October values. Beta **1.75**, pretax borrowing cost **5.5%** and tax **20%** are explicit judgments. With common market equity, NCI proxy and gross debt plus finance leases, calculated WACC is about **11.79%**, rounded to **11.8%**. Sources: the URLs retained in `project1/research.py` and `docs/assumption-challenge-record.md`.
- New bridge items: lease Note 9 reports finance lease present value **14.233** separately from operating lease liabilities **316.210**; pension Note 11 reports **22 + 27 = 49** of deficits. They are not added to the gross debt principal a second time. Operating leases remain operating expenses. These adjustments correct incomplete scope in the earlier AI-assisted draft; they are source/definition checks, not evidence that the earlier draft was investment-ready.
- Historical checks now include the reported cash-flow identity **1,632.913 + 79.514 − 1,413.724 + 1,477.076 − 7.383 = 1,768.396**, including restricted cash, and the normalized core EBIT bridge **897.861 + 63.390 + 64.404 − 124.133 = 901.522**. Cash-flow and balance-sheet cash bases are explicitly reconciled.
- **Official known-answer check:** `test_official_course_training_answers` matches all twelve published Lab 05 outputs within 0.0001, including EV **1,624.8685**, equity **1,374.8685**, diluted value/share **27.4974** and terminal share **0.7240**. It also checks published sensitivity-grid corners within one cent. Source: https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md . This completes the course-training reconciliation that the earlier synthetic annuity alone did not establish.
- **Peer policy/definition check:** original policy retained. FN's filing supports **47.9% + 33.3% = 81.2%** nonoverlapping qualifying revenue and multi-continent operations. Price × disclosed June actual shares gives approximately **USD 13.43bn** market cap, above the threshold, with share-date lag disclosed. Reported annual GAAP diluted P/E is equity/equity; EV/sales and EV/EBITDA use a common cash-retention rule and operating-lease treatment. LITE is not called a verified policy pass because its revenue-mix check remains unresolved. FN-only references are not a diversified peer range.
- **Highest-risk failure test:** higher growth alone and sticky-capex downside expose funding shortfalls rather than silently adding financing. Debt maturity narrative/table inconsistencies, springing maturities and the excluded restricted-use subsidiary facility qualify interpretation. A model funding failure is not a claim of company insolvency.
- **Cold run:** `outputs/cold-run-20261019T231649Z.txt`, UTC October 19, 2026 23:16:49. `project1/cold_run.py` copied only required source files into a new directory, verified hashes, created a fresh virtual environment without pip, ran all six finance tests, generated full output and exported the visible HTML. All commands exited 0; base checks passed; the failed stress remained failed. No third-party packages were installed. This is a recorded text-log AI-assisted clean run, not a student AI-closed run or a recorded video.
- **Terminal challenge:** alternative return-on-new-capital assumptions of 8/12/16%, holding the base forecast and WACC fixed, produce approximately **USD 56/68/73 per share**. The base capital-growth terminal convention remains explicit and is not averaged with these challenge cases.
- **Material AI dispositions in development:** corrected the disconnected/positive-only valuation for this project's signed-FCFF architecture; corrected the incomplete bridge; qualified funding-failure and peer-range interpretations; retained the student's operating paths; proposed a transparent judgment-dependent WACC and causal cases. Nicolas has explicitly reaffirmed the operating paths. His final review of remaining finance judgments and written artifacts is pending. Named tool: **OpenAI Codex**; exact underlying model/version was not exposed to this session and is not invented.
- **Review artifacts:** `docs/decision-memo.md`/`.pdf`, `docs/research-evolution.md`/`.pdf` and `docs/evidence-ledger.csv` are review drafts. Research-Evolution includes the faithful presumed Edition A conversion first; no checkpoint receipt or clean authorship is asserted. PDFs must be regenerated after final Markdown changes before freezing.

### September 15 valuation-date decision and FCFF integration

- Nicolas selected September 15, 2026 as the final valuation date and information cutoff during October 19 final preparation. Original Edition A dates remain unchanged. Later retrieval of sources is verification, not permission to use post-cutoff events in the investment judgment.
- Codex created `project1/engine.py`, `project1/test_engine.py`, `project1/app.py` and `project1/README.md` alongside the preserved labs. These are new AI-authored implementation files; Nicolas has not yet completed ownership review or adopted their provisional valuation assumptions.
- Five new finance tests passed: a synthetic constant-perpetuity known answer and negative-cash-flow retention; articulation/FCFF identity/equity bridge and restoration; predeclared Codex directional tests across the WACC–growth grid; genuine funding failure and invalid input rejection; reverse-DCF target reconstruction. The synthetic check is independently constructed and does not substitute for the required reconciliation to published course training-case answers.
- The directional predictions in `test_engine.py` were written before execution by Codex. They are AI-assisted tests and are not represented as the student's AI-off Locked Changed-Input Record.
- Generated visible outputs: `outputs/project1-base.md`, `outputs/project1-base.json`, and `outputs/project1-visible-output.html`. Provisional base: USD 86.65 per actual common share (consult full-precision JSON); EV approximately USD 18,873.800 million; terminal PV/EV approximately 88.43%. WACC 11% and terminal growth 3% remain judgments requiring review.
- The interface was served at loopback `127.0.0.1:8501`. HTTP checks verified margin +1 pp produces approximately USD 92.16/share with passing checks; growth +5 pp produces approximately USD 105.75/share as a funding-invalid conditional diagnostic; base restoration returns approximately USD 86.65/share with passing checks. These checks were AI-assisted, in the existing environment.
- Safari displayed the base interface, its actual-common-share label, statements, passing checks and sensitivity tables. Attempts at further UI interactions were interrupted by computer-use focus changes; a complete on-screen slider/stress/reset rehearsal remains outstanding. No recording or clean-environment cold run is claimed.
- No new packages were installed. Implementation uses the Python standard library. June 30 balance-sheet proxies, August 10 actual common shares, USD 300 million retained operating cash, September 15 first-year stub convention, NCI proxy, operating-lease convention and terminal reinvestment transition are disclosed in the new README and output. Capex/inventory/WACC/g stress bounds beyond prior growth/margin choices are proposed, not student-approved.

### October 19 integration audit

- Codex executed the original pro-forma with `--self-test`: exit 0; base-year balance-sheet reconstruction and all five forecast articulation/funding checks passed. The original model and assumptions were not edited.
- Codex executed `Proforma Financial Analysis/test_cohr_sensitivity.py`: all five tests passed.
- Codex derived signed FCFF from operating inputs and independently reconciled it through CFO, adjusting for cash-interest and debt-cost tax effects; all five years agreed within USD 0.00000001 million under current assumptions.
- Codex independently opened the FY2026 SEC filing and company annual release. Filing revenue, separate unusual operating items, NCI, and August 10 common shares corroborate the inspected local source material.
- Detailed findings, formula definitions, limitations, and outstanding work: `docs/project-1-audit.md`.
- These are AI-assisted checks, not the AI-closed Locked Changed-Input Record or a fresh-environment cold run. No completed company valuation or final recommendation is claimed by this audit.

This working record is incomplete. Financial validation, source checks, locked changed-input evidence, cold-run results, and additional AI-output checks will be added as they are reviewed or performed. No unverified historical test or receipt is represented as completed.


## Final packaging and recorded evidence — October 19, 2026

OpenAI Codex prepared timestamped transcripts from the final Zoom VTT captions, corrected obvious recognition errors using the displayed code and finance terminology, and preserved the original captions. No audio comparison or student transcript review is asserted by this preparation. Recordings were not edited. Actual MP4 container durations: Video 1 163.920 seconds; Video 2 313.323 seconds; Video 3 209.045 seconds. Video 2 exceeds the five-minute grading window; its full transcript includes remarks after that cutoff.

The finance tests were re-executed successfully during recording preparation, including the targeted funding-failure test and the two Video 1 checks. The +5 percentage-point growth stress has a FY2030 cash-floor shortfall of USD 313.79 million; its model failure is expected by the passing test. These remain AI-assisted verification activities.

The new submission repository preserves prior Git history and packages the runnable source, historical labs, visible outputs, PDFs, source records, and transcripts. A dependency file explicitly states Python 3.10+ and standard-library-only application requirements. No credentials are required. Videos hosted in GitHub Pages are supplementary access copies; they do not establish compliance with the requirement for YouTube or an approved Purdue host. Student confirmation of official video URLs, transcript review, final finance judgments, and the Brightspace receipt is not asserted. The original Edition A and historical changed-input provenance qualifications above remain in force.
