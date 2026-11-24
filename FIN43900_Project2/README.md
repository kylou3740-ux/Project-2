# FIN 43900 Project 2 — Investment Committee Portfolio

**AI-use statement:** ChatGPT (OpenAI) was used for planning, coding assistance, and drafting. I reviewed the outputs and am responsible for checking the data, analysis, interpretation, and final decision.

**Educational statement:** This application is an academic exercise, not investment advice.

## Committee decision question
Can a transparent, momentum-ranked allocation process be considered for a small pilot under the Investment Committee Portfolio mandate, compared with two transparent baselines?

## Mandate carried forward from Lab 13
- Portfolio reference size: $100 million.
- Quarterly distribution: $750,000.
- Investment horizon: 7 years.
- Objective: CPI + 4% net over rolling five-year periods.
- Reference benchmark: 60% global equities / 40% investment-grade bonds.
- Long-only, no borrowing or derivatives.
- Reserve: minimum 3%.
- Liquidity: at least 90% redeemable within five business days.
- Issuer concentration: no company above 8%.
- Turnover: 25% annual maximum absent approval.
- Calendar-year loss rule: 10%; interpretation remains unresolved.

## Asset proxies
SGOV (Treasury-bill/reserve proxy), IEF (Treasury 10-year proxy), AGG (investment-grade bond proxy), and ACWI (global equity proxy). ETF proxies are not identical to direct asset holdings; proxy selection is a limitation.

## Portfolios compared
1. Equal-weight baseline.
2. Inverse-volatility baseline over risk sleeves.
3. Constrained momentum portfolio: reserve minimum plus two highest-ranked risk sleeves; grid-search lowest volatility subject to the selected estimated-return hurdle and reserve floor. The app refuses an allocation if the optimizer is infeasible. The 60/40 benchmark is shown as mandate context.

## Point-in-time signal
12–1 momentum: price return over the selected lookback ending one complete month before the cutoff. Data are cutoff-filtered to the chosen date, but Yahoo Finance is not a historical-vintage archive. Therefore, the signal is not fully point-in-time validated against data revisions or vendor availability.

## Run locally (Windows PowerShell)
1. Install Python 3.11+.
2. Open this folder in VS Code and create a virtual environment: `py -m venv .venv`
3. Activate: `.venv\Scripts\Activate.ps1`
4. Install: `pip install -r requirements.txt`
5. Run: `python -m streamlit run app.py`

Internet access is required for the Yahoo Finance download. If the data download fails, the app displays an error rather than inventing results.

## Tests
Run: `python -m unittest discover -s tests -v`

## Stop / review conditions
Do not proceed to a portfolio recommendation if the optimizer is infeasible, coded checks fail, data cannot be reproduced at the selected cutoff, a hard mandate requirement cannot be verified, or allocations are unstable under reasonable input/window changes. The app reports several hard mandate checks as unverified; passing coded checks is not a full mandate pass.

## Repository map
- `app.py`: Interactive Streamlit interface and data retrieval
- `portfolio_core.py`: Transparent calculations and optimizer
- `docs/data-card.md`: Data provenance and methodology
- `docs/decision-memo.md`: Investment committee recommendation and analysis
- `docs/validation-and-ai-use.md`: Validation results, stress testing, limitations, and AI disclosure, includes locked changed-input record
- `docs/cold-run-record.md`: Partner cold-run documentation
- `docs/manifest.md`: Links and deliverables checklist

## Video Presentations

1. **Video 1 — https://youtu.be/xdn9tBAj5bU 
2. **Video 2 — https://youtu.be/xdn9tBAj5bU
3. **Video 3 — https://youtu.be/o38BFEYRJD4
