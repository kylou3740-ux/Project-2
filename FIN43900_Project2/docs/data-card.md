# Data Card — Project 2

## Purpose
Price data are used to estimate monthly returns and volatility, rank risk sleeves using momentum, and compare portfolios.

## Series / ETF proxies
| Sleeve | Symbol | Proxy caveat |
|---|---|---|
| Treasury bills / reserve | SGOV | Short-duration Treasury ETF proxy |
| Treasury 10-year | IEF | Intermediate Treasury exposure; not a pure 10-year note |
| Investment-grade bonds | AGG | Broad U.S. investment-grade bond ETF |
| Global equities | ACWI | Broad global equity ETF |

## Source, retrieval, cutoff
Yahoo Finance, accessed through `yfinance` when the app runs. User-selected as-of cutoff is applied to retrieved daily prices. The app reports the last retrieved price date. The source is not a vintage-controlled database and does not prove what was available to an investor on that historical date.

## Transformations
- Download adjusted prices (`auto_adjust=True`).
- Forward-filling may create repeated prices for dates without new observations and can affect calculated returns or volatility.
- Resample to month-end prices and calculate percentage returns.
- Estimate annual arithmetic return as monthly mean × 12.
- Estimate annual volatility as monthly sample standard deviation × √12.
- Momentum is cumulative price change across the selected lookback ending one completed month before the cutoff (skips the most recent month).
- Transaction costs are modeled as a one-time deduction from the first monthly portfolio return rather than recurring costs applied to each rebalance.

## Known limitations
- No formal archived vendor vintage: cutoff-filtering is not equivalent to fully point-in-time provenance.
- Proxy ETFs are not the same as direct asset classes.
- No complete holdings look-through concentration test.
- Liquidity and redemption timing are not proven by ETF daily prices.
- Calendar-year loss restriction is not fully implemented; mandate definition is unresolved.
- Rolling five-year CPI+4% objective is not validated.
- Return estimates are historical, sensitive, and not forecasts.
- Costs are simplified and not a complete bid/ask, tax, market-impact, or recurring-fee model.
