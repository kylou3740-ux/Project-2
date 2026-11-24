# Project 2 — Investment Committee Decision Memo

**Project:** FIN 43900 — Investment Management Application  
**Prepared by:** Student Portfolio Analyst  
**As-of date:** November 23, 2026  
**Intended audience:** Investment Committee  
**Decision:** Pilot / Defer Full Adoption

---

## 1. Executive Summary

This analysis evaluates whether a constrained momentum portfolio should be considered for adoption within a portfolio mandate emphasizing long-term growth, income requirements, risk management, and liquidity.

The application compares an equal-weight portfolio, an inverse-volatility portfolio, and a constrained momentum portfolio using historical market data, portfolio-level performance and risk statistics, selected mandate constraints, and a transaction-cost sensitivity test.

The constrained momentum portfolio demonstrated the strongest historical results among the three portfolios in the displayed sample, with the highest annualized historical return, the lowest annualized volatility, and the least severe maximum drawdown. However, the results are historical estimates and do not demonstrate that the strategy will outperform in future market conditions. Several important mandate requirements also remain unverified by the application.

**Recommendation: PILOT / DEFER FULL ADOPTION.** The strategy warrants further investigation, but the evidence is insufficient to support unconditional adoption. Any pilot should be subject to committee approval, additional validation, and completion of outstanding mandate checks.

---

## 2. Investment Mandate and Decision Context

The portfolio mandate is designed to support a $100 million portfolio with quarterly distributions of $750,000 while pursuing a long-term return objective of CPI plus 4%.

Key mandate parameters include:

- **Portfolio size:** $100 million
- **Quarterly distribution requirement:** $750,000
- **Return objective:** CPI + 4%
- **Evaluation period:** Rolling five-year periods
- **Investment horizon:** Seven years
- **Reference benchmark:** 60% global equities / 40% investment-grade bonds
- **Minimum reserve allocation:** 3%
- **Liquidity requirement:** At least 90% redeemable within five business days
- **Issuer concentration limit:** Maximum 8%
- **Turnover limit:** 25% annually without approval

The application uses four ETFs as asset-class proxies:

| ETF | Portfolio role |
|---|---|
| BIL | Treasury bills / reserve |
| IEF | Treasury bonds |
| LQD | Investment-grade corporate bonds |
| VT | Global equities |

The investment question is whether a constrained momentum strategy provides a sufficiently attractive historical risk-return profile to justify further consideration relative to simpler portfolio construction alternatives.

---

## 3. Portfolio Alternatives

Three portfolio construction approaches were evaluated.

### Equal-Weight Baseline

The equal-weight baseline allocates equally across the four portfolio sleeves. It provides a transparent reference point and avoids relying on an optimization process or momentum signal to determine portfolio weights.

### Inverse-Volatility Baseline

The inverse-volatility baseline allocates based on estimated asset volatility, assigning relatively greater weight to assets with lower estimated volatility. This provides a risk-oriented alternative to equal weighting.

### Constrained Momentum Portfolio

The constrained momentum portfolio uses a momentum signal to rank risk sleeves and applies portfolio constraints to determine the allocation. The signal is based on cumulative price return over the selected lookback period, ending one full month before the data cutoff.

The signal is used as a portfolio-ranking mechanism. It is not presented as proven alpha or as evidence of future outperformance.

---

## 4. Historical Performance and Risk Evidence

The application displayed the following results under the 50-basis-point transaction-cost setting:

| Portfolio | Annualized Historical Return | Annualized Volatility | Maximum Drawdown |
|---|---:|---:|---:|
| Equal-Weight Baseline | 3.27% | 6.66% | -14.05% |
| Inverse-Volatility Baseline | 1.61% | 7.93% | -17.08% |
| Constrained Momentum Portfolio | 6.46% | 6.02% | -10.48% |

In the displayed sample, the constrained momentum portfolio produced the highest annualized historical return and the lowest annualized volatility and maximum drawdown among the three alternatives.

These results provide a favorable historical comparison for the constrained momentum approach. However, the observed performance is dependent on the sample period, historical data, portfolio assumptions, signal methodology, and implementation assumptions. The results do not establish that the strategy will outperform the baselines in future periods.

The portfolio should therefore be evaluated based on the overall quality of its evidence, not solely on its historical performance ranking.

---

## 5. Transaction-Cost Sensitivity

A changed-input test evaluated the transaction-cost assumption by comparing a 0-basis-point configuration with a 50-basis-point configuration.

The 50-bps configuration displayed the following annualized historical returns:

| Portfolio | 0 bps | 50 bps |
|---|---:|---:|
| Equal-Weight Baseline | 3.37% | 3.27% |
| Inverse-Volatility Baseline | 1.71% | 1.61% |
| Constrained Momentum Portfolio | 6.56% | 6.46% |

The displayed results corresponded with approximately a 0.10-percentage-point decrease in annualized historical returns across all three portfolios when comparing the two configurations. Volatility changed slightly for the equal-weight and constrained momentum portfolios, while the inverse-volatility portfolio's displayed volatility remained unchanged. Maximum drawdown and portfolio allocations remained unchanged in the displayed results.

The comparison was conducted retrospectively, and the displayed data cutoffs were not confirmed to be identical between runs. Therefore, the comparison is directionally consistent with the expectation that higher transaction costs reduce returns, but it should not be interpreted as an isolated causal measurement of the transaction-cost effect.

The stress test reinforces the need to examine implementation assumptions and costs before adopting the strategy.

### Correction to Locked Changed-Input Record

After the locked changed-input record was committed, I identified an error in the recorded original transaction-cost value. The locked record states that the original value was 10 basis points (bps), but the application's actual starting transaction-cost setting was 0 bps. The application was subsequently run using a 50-bps transaction-cost setting.

The original locked record has been preserved without modification to maintain the integrity of the pre-test record. This correction is documented transparently rather than retroactively changing the original submission.

For purposes of interpreting the application results, the actual input comparison was **0 bps to 50 bps**, not 10 bps to 50 bps. The original prediction remains preserved as written, and this discrepancy is considered when evaluating the experiment's limitations and results.

---

## 6. Mandate Compliance, Risks, and Limitations

The application evaluates selected portfolio constraints and reports pass/fail results for coded rules. However, an overall mandate pass is not established because several requirements are not fully verified.

Outstanding mandate checks include:

- ETF look-through issuer concentration against the 8% limit
- Liquidity sufficient to meet the five-business-day requirement
- Annual turnover against the 25% limit
- The 10% calendar-year loss rule

These requirements are reported as unverified rather than assumed to be satisfied.

Additional limitations include:

- Historical performance may not represent future results.
- ETF proxies may not perfectly represent the intended asset-class exposures.
- Transaction-cost assumptions may not reflect actual trading costs or market impact.
- Portfolio optimization results are sensitive to assumptions and estimation choices.
- Historical results may vary depending on the evaluation window.
- Momentum signals may not remain effective across different market environments.

The application is a decision-support prototype. It does not replace independent financial analysis, complete due diligence, or committee judgment.

---

## 7. Recommendation and Conditions for Further Consideration

### Recommendation: PILOT / DEFER FULL ADOPTION

The constrained momentum portfolio merits further investigation based on its favorable historical results relative to the two baselines. However, full adoption is not recommended at this stage because the strategy's historical performance is not sufficient to establish future suitability, and several important mandate requirements remain unverified.

An illustrative pilot range of **0–10% of reserve assets** may be considered only after committee approval, additional data verification, and completion of the outstanding mandate checks. This range is a judgment-based proposal for further consideration and is not an optimizer output or a mandate-approved allocation.

### Conditions before adoption or expansion

Before the strategy is adopted or expanded, the following should be completed:

1. Verify ETF underlying holdings and aggregate issuer concentration.
2. Confirm liquidity against the five-business-day mandate requirement.
3. Evaluate annual turnover and confirm compliance with the turnover limit.
4. Verify the calendar-year loss constraint.
5. Review the sensitivity of the strategy to historical window selection, signal assumptions, and implementation costs.
6. Confirm that the data, portfolio construction methodology, and application outputs can be reproduced.

### Monitoring and reversal triggers

Further consideration should be suspended or the strategy reviewed if:

- Data sources or historical inputs cannot be reproduced.
- A hard mandate constraint fails.
- The reserve or liquidity requirement is breached.
- The optimizer becomes infeasible.
- Portfolio allocations change materially under small assumption or window changes.
- Actual implementation costs materially exceed the assumed level.
- The momentum signal or supporting evidence deteriorates materially.

---

## 8. Committee Action Requested

The committee is requested to **approve further investigation and, if appropriate, a limited pilot subject to the conditions above—not full adoption of the strategy**.

The current evidence supports continued evaluation but does not establish full mandate compliance or demonstrate reliable future outperformance.

---

## AI Use Disclosure

AI tools were used as assistance during project development, including coding support, debugging, organization, and drafting/review of documentation. AI-generated suggestions were reviewed and evaluated. The analytical judgments and final recommendation are the student's own. The complete material AI-use record and validation evidence are provided in the accompanying Validation and AI Use Record.

---

## Educational Disclaimer

This project was developed for educational purposes as part of FIN 43900. It is not investment advice. Historical performance, model outputs, and assumptions do not guarantee future results.
