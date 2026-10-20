# COHR — Project 1 Corporate Finance Application

[Submission portal](https://nicocerioni-creator.github.io/FIN439-Project1-COHR-Submission/index.html) · [Manifest and video evidence index](docs/submission-manifest.md)

Videos: [Video 1](https://youtu.be/RJJ-qHn8fPE), [Video 2](https://youtu.be/KrhwmjNDZBg), [Video 3](https://youtu.be/wsCrWOBVG38). These are the official YouTube submissions. Supplementary MP4 copies are included in `videos/` and the submission portal. Corrected caption-derived transcripts and original captions are in `docs/`.

**Decision:** watch/defer for a buy-side committee with no current position; prospective 3–5-year horizon. Valuation date and information cutoff: **September 15, 2026**. USD, actual common-share basis. The passing causal DCF range is approximately **$45–$154/share**, base **$75.60**, versus a dated market reference of **$271.17**. This is an individual FIN 43900 academic project. The decision memo governs the written recommendation.

## Run and reproduce

Python 3.10+; the application and finance tests use only the standard library. No package installation, credentials or network data retrieval is required. From the repository root:

```sh
python3 project1/test_engine.py
python3 project1/engine.py
python3 project1/app.py
```

Open http://127.0.0.1:8501. Stop with Ctrl+C. Use `--port 8502` if needed. `python3 project1/app.py --export` rebuilds the saved visible HTML. `python3 project1/cold_run.py` makes a fresh copy and virtual environment without installing packages, tests and exports it, and preserves a timestamped log.

## Open without running

- [Executed report](outputs/project1-base.md), [complete model output](outputs/project1-base.json), and [saved workbench](outputs/project1-visible-output.html). Driver changes require the local server.
- [Decision memo PDF](docs/decision-memo.pdf) and [source](docs/decision-memo.md).
- [Research evolution PDF](docs/research-evolution.pdf), including the unchanged presumed Edition A conversion and its provenance qualification.
- [Validation and named AI-tool disclosure](docs/validation-and-ai-use.md); its submission PDF must match the final working record.
- [Assumption challenges](docs/assumption-challenge-record.md), [sensitivity interpretation](docs/proforma-sensitivity-interpretation.md), and [evidence ledger](docs/evidence-ledger.csv).
- [Recording guide](docs/recording-guide.md). Guides are not actual video transcripts.

## Repository and data flow

`project1/app.py` supplies bounded controls, reset and visible checks. `project1/engine.py` imports the unchanged `Pro-Forma Financial Statements/proforma.COHR.py`, then derives signed FCFF, scenarios, sensitivities and the common-equity bridge. `project1/research.py` contains dated facts, source locators, WACC and peer definitions. `project1/test_engine.py` contains financial tests. Original lab folders remain historical evidence; their FCFE conventions and earlier values do not govern the integrated FCFF result. The earlier README is preserved in `docs/archive/README-before-project1-integration.md`.

## Sources, assumptions and limitations

Material history is traced to the FY2026 COHR and Fabrinet SEC filings, company releases, dated Treasury yields and Damodaran ERP data; exact URLs and dates appear in the evidence ledger and research source. Forecasts, judgment beta, borrowing cost, retained cash and terminal conventions are identified separately from facts. June cash/debt and August common shares are dated proxies at September 15; first-year FCFF uses an explicit partial-year convention. SBC remains an expense. The bridge includes debt, NCI, finance leases and pension deficits; restricted cash is excluded. No credentials are required, so no .env file is needed.

Terminal value is 87.4% of base EV. Capacity utilization, cash conversion and concentrated customers carry material downside risk. Datacenter & Communications is 74.1% of revenue, not a verified AI-only percentage. A failed funding check makes a conditional valuation diagnostic, not a passing investment case. Single-peer references are not a diversified valuation range. Historical Edition A and AI-off evidence limits are disclosed without recreating a checkpoint or claiming unaided authorship of AI-assisted integration work. Video links, caption-derived corrected transcripts and the evidence manifest are included. Student audio review, final judgment review and the Brightspace receipt remain unverified.
