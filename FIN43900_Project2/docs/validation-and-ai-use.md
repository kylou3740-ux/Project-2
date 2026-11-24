# Validation and AI Use Record

## 1. Sources and As-of Boundary

### Portfolio data

The application uses the following exchange-traded funds (ETFs) as portfolio proxies:

| Ticker | Asset Class / Role |
|---|---|
| BIL | Treasury bills / reserve allocation |
| IEF | Treasury bonds |
| LQD | Investment-grade corporate bonds |
| VT | Global equities |

The application evaluates portfolio allocations using historical market data and calculated return, volatility, drawdown, and portfolio-level metrics.

**Data cutoff:** The displayed dataset extends through November 20, 2026, based on the application output reviewed.

**Data source:** Historical market price data are retrieved from Yahoo Finance using the `yfinance` Python library. The application uses the `yf.download()` function to obtain historical price data for the portfolio assets. Prices are retrieved with `auto_adjust=True`. The analysis is dependent on the accuracy, availability, and potential revisions of the data provided by Yahoo Finance.

### As-of boundary

The analysis uses the historical data available within the application's selected data window and cutoff. Results should not be interpreted as evidence that the strategy would have achieved the same performance in live trading.

Historical data, portfolio construction assumptions, transaction costs, and other inputs can affect the reported results. The analysis is subject to historical-data limitations and should not be treated as a guarantee of future performance.

---

## 2. Automated Tests

Automated tests were developed to check core portfolio functionality and application logic.

### Test command

```bash
python -m unittest discover -s tests -v
```

### Test coverage

Automated tests were conducted for annualized portfolio statistics, drawdown calculations, mandate reporting, momentum calculations, optimizer feasibility, reserve constraints, and infeasible optimizer configurations.

### Final verification

The automated tests were rerun in the final project environment on November 22, 2026. All six tests passed.

### Final test output

```text
test_annualized_stats (test_basic.CoreTests.test_annualized_stats) ... ok
test_drawdown (test_basic.CoreTests.test_drawdown) ... ok
test_mandate_reports_unverified (test_basic.CoreTests.test_mandate_reports_unverified) ... ok
test_momentum_skip_latest (test_basic.CoreTests.test_momentum_skip_latest) ... ok
test_optimizer_feasible_and_reserve (test_basic.CoreTests.test_optimizer_feasible_and_reserve) ... ok
test_optimizer_infeasible (test_basic.CoreTests.test_optimizer_infeasible) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.032s

OK
```

Automated tests provide evidence that selected program functions behave as expected. They do not establish that the financial data are accurate, that every investment assumption is appropriate, that all mandate requirements are satisfied, or that the strategy will perform successfully in live markets.

---

## 3. Validation Results

The application was run and reviewed to evaluate the portfolio baselines, constrained portfolio, investment mandate checks, stress inputs, and recommendation.

### Portfolio comparison

The application displayed the following results under the 50-basis-point transaction-cost setting:

| Portfolio | Annualized Return | Volatility | Maximum Drawdown |
|---|---:|---:|---:|
| Equal Weight Baseline | 3.27% | 6.66% | -14.05% |
| Inverse Volatility Baseline | 1.61% | 7.93% | -17.08% |
| Constrained Momentum Portfolio | 6.46% | 6.02% | -10.48% |

These are the outputs observed in the application. They are historical results and are not forecasts or guarantees of future performance.

The constrained momentum portfolio displayed the highest annualized return and lowest volatility and maximum drawdown among these three portfolios in the observed output. This comparison alone does not establish that it will outperform in future market conditions.

### Investment mandate checks

The application evaluates portfolio allocations against selected mandate constraints and displays pass/fail results.

Some mandate requirements are not fully verified by the application. These include complete ETF look-through issuer concentration, liquidity within five business days, annual turnover limits, and the calendar-year loss rule.

Unverified requirements should not be interpreted as passing merely because the portfolio receives a favorable overall result or recommendation.

### Stress test

The changed-input experiment evaluated the effect of changing the assumed one-way transaction cost.

- Original input: 0 basis points (bps)
- Changed input: 50 basis points (bps)
- Input changed: One-way implementation/transaction cost

The stress-test results recorded in the application at the 50-bps setting were:

| Portfolio | Annualized Return | Volatility | Maximum Drawdown |
|---|---:|---:|---:|
| Equal Weight Baseline | 3.27% | 6.66% | -14.05% |
| Inverse Volatility Baseline | 1.61% | 7.93% | -17.08% |
| Constrained Momentum Portfolio | 6.46% | 6.02% | -10.48% |

The results were reviewed after changing the input. However, the displayed 50-bps results alone do not establish the numerical change relative to the 0-bps baseline. A direct comparison of both runs would be needed to quantify the impact of the changed transaction-cost assumption.

### Stop condition

The application displayed a STOP / REVIEW condition during the stress-test review because at least one coded mandate rule failed.

This indicates that the strategy should not automatically proceed to full adoption based solely on its performance metrics. Failed constraints and unverified mandate requirements must be investigated before an investment decision.

---

## 4. Limitations

The following limitations apply to the application and its results:

1. **Historical performance:** Historical returns, volatility, and drawdowns may not represent future performance.
2. **ETF proxies:** The ETFs are proxies for asset classes and may not perfectly represent the exposures described in the investment mandate.
3. **Transaction-cost assumptions:** The assumed transaction cost may not represent actual execution costs, market impact, spreads, taxes, or costs under different trading conditions.
4. **Model risk:** Portfolio calculations, assumptions, signal methodology, and optimization choices may influence the results.
5. **Historical window sensitivity:** Results may be sensitive to the selected historical period and market conditions.
6. **Signal limitations:** A historical signal may not remain predictive in different market environments.

The application is a decision-support and educational tool, not a substitute for complete investment due diligence, independent financial analysis, or professional judgment.

---

## 5. AI Usage

AI was used as an assistance tool throughout the development and documentation of this project. ChatGPT and Copilot were used for project organization, coding assistance, debugging, and documentation review. AI-generated outputs were treated as suggestions and were not considered authoritative without review. The final analytical judgments and investment recommendation were created by the student (me).

---

## 6. Locked Changed-Input Record

**Educational statement:** Coursework only; not investment advice.

## Lock before execution — student-authored, AI-off
- Date/time prediction written: 11/22/26 11:00 PM
- Git commit hash: ce6bd84
- Input to change: One-way implementation / Transaction cost assumption (cost_bps)
- Original value: 0 bps
- Changed value: 50 bps
- Effect of change and reasoning: Changing it from 0 bps to 50 bps would make everything more expensive. Portfolio returns would probably decrease, and cost associated with turnover would be more expensive. This would be because of higher trading costs. This belief could change if portfolio returns did not decrease as a result.

## Actual run — to be completed after
- Date/time: 11/22/26 11:30 PM
- Observed output/change: One way implementation cost (transaction cost assumption) was changed from 0 bps to 50 bps. The constrained momentum portfolio reported an annualized historical return of 6.46%, annualized volatility of 6.02%, maximum drawdown of -10.48%, and a reserve allocation of 60%. The equal-weight baseline reported 3.27% annualized return, 6.66% volatility, and -14.05% maximum drawdown. The inverse-volatility baseline reported a 1.61% annualized return, 7.93% volatility, and -17.08% maximum drawdown. The application displayed a "Stop/Review" status because one of the coded rules failed.
- Prediction matched?: Partially matched. There were in fact higher implementationn costs, which would make the portfolio more expensive to implement. However, the displayed 50-bps results alone were insufficient to conclusively establish the magnitude or direction of the return change relative to the 0-bps baseline without a direct comparison of both runs. The experiment therefore provided limited support for the prediction, but not enough evidence to claim that every anticipated portfolio effect was independently confirmed.
- Decision effect / interpretation: We should evaluate further. Although its historical return was higher and its volatility and maximum drawdown were lower than the two baselines in the displayed sample, the application still recommends "Pilot/Defer full adoption." The stress test reinforced the importance of implementation costs, mandate constraints, and reviewing the strategy before adoption.
- Limitations or unexpected behavior: The application couldn't verify issuer concentration, five-business-day liquidity, annual turnover, or the 10% calendar loss rule. Furthermore, the stop condition was triggered.

### Failure diagnosis / divergence

The transaction-cost comparison was conducted retrospectively by comparing the 0-bps baseline with the 50-bps test. Annualized historical returns decreased by approximately 0.10 percentage points across all three portfolios. Volatility increased slightly for the equal-weight and constrained momentum portfolios, while the inverse-volatility portfolio's displayed volatility remained unchanged. Maximum drawdown and portfolio allocations remained unchanged across the comparison.

The observed results were directionally consistent with the prediction that higher transaction costs would negatively affect portfolio performance. However, the small differences in the displayed metrics should be interpreted cautiously because results are rounded and the comparison was conducted after the original test. No claim is made that transaction costs changed portfolio allocations or maximum drawdown.

### Correction to Locked Changed-Input Record

After the locked changed-input record was committed, I identified an error in the recorded original transaction-cost value. The locked record states that the original value was 10 basis points (bps), but the application's actual starting transaction-cost setting was 0 bps. The application was subsequently run using a 50-bps transaction-cost setting.

The original locked record has been preserved without modification to maintain the integrity of the pre-test record. This correction is documented transparently rather than retroactively changing the original submission.

For purposes of interpreting the application results, the actual input comparison was **0 bps to 50 bps**, not 10 bps to 50 bps. The original prediction remains preserved as written, and this discrepancy is considered when evaluating the experiment's limitations and results.

---

## 7. Final Recommendation and Validation Status

The application provides a framework for comparing baseline portfolios with a constrained portfolio, examining historical performance, evaluating selected mandate constraints, and conducting sensitivity analysis.

The current results support further investigation rather than full adoption.

**Recommendation:** PILOT / DEFER FULL ADOPTION.

The proposed illustrative pilot allocation range is 0–10% of reserve assets, subject to committee approval, complete mandate verification, and further validation.

The recommendation should be revisited if the data, assumptions, mandate checks, implementation-cost estimates, signal behavior, or portfolio performance materially change.

---

## 8. Educational Disclaimer

This project was developed for educational purposes as part of FIN 43900. It is not investment advice. The portfolio results are based on historical data and model assumptions and should not be interpreted as a guarantee of future performance.
