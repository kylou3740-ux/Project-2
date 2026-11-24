"""Transparent calculations for FIN43900 Project 2."""
import numpy as np
import pandas as pd

def annualized_stats(monthly_returns):
    r=monthly_returns.dropna()
    if len(r)<2: return np.nan,np.nan
    return float(r.mean()*12),float(r.std(ddof=1)*np.sqrt(12))

def max_drawdown(returns):
    r=returns.dropna()
    if r.empty: return np.nan
    wealth=(1+r).cumprod()
    return float((wealth/wealth.cummax()-1).min())

def momentum_12_1(month_end_prices, lookback_months=12):
    """Price momentum ending one month before the most recent month-end: t-1 vs t-(lookback+1)."""
    p=month_end_prices.dropna()
    if len(p)<lookback_months+2: return pd.Series(dtype=float)
    end=p.iloc[-2]
    start=p.iloc[-(lookback_months+1)]
    return end/start-1

def optimize_min_vol(expected_returns,covariance,eligible,min_reserve,target,step=0.05):
    assets=list(expected_returns.index)
    units=round(1/step)
    best=None
    def rec(remaining,n,prefix=()):
        if n==1: yield prefix+(remaining,)
        else:
            for x in range(remaining+1): yield from rec(remaining-x,n-1,prefix+(x,))
    for integer_weights in rec(units,len(assets)):
        w=np.asarray(integer_weights,dtype=float)/units
        exp=float(w@expected_returns.values)
        reserve=sum(w[i] for i,a in enumerate(assets) if a in eligible)
        if exp+1e-12<target or reserve+1e-12<min_reserve: continue
        variance=float(w@covariance.values@w)
        vol=float(np.sqrt(max(variance,0)))
        if best is None or vol<best["vol"]:
            best={"weights":pd.Series(w,index=assets),"expected_return":exp,"vol":vol,"reserve":float(reserve)}
    return best

def portfolio_metrics(weights,monthly_returns,cost_bps=0):
    r=monthly_returns[list(weights.index)].mul(weights,axis=1).sum(axis=1)
    # Apply assumed one-time cost to the first period only; it is not a recurring annual fee.
    if len(r): r.iloc[0]-=cost_bps/10000
    ar,av=annualized_stats(r)
    return {"returns":r,"annualized_return":ar,"annualized_volatility":av,"max_drawdown":max_drawdown(r)}

def mandate_verdict(weights,reserve_min=0.03):
    checks=[]
    weights=weights.astype(float)
    checks.append("PASS weights sum to 100%" if np.isclose(weights.sum(),1.0,atol=1e-6) else "FAIL weights do not sum to 100%")
    checks.append("PASS long-only" if (weights>=-1e-10).all() else "FAIL negative/short weights")
    reserve=float(weights.get("Treasury bills / reserve",0))
    checks.append(f"PASS reserve floor ({reserve:.1%} ≥ {reserve_min:.1%})" if reserve+1e-9>=reserve_min else f"FAIL reserve floor ({reserve:.1%} < {reserve_min:.1%})")
    fails=[x for x in checks if x.startswith("FAIL")]
    unverified=["ETF look-through issuer concentration (8% limit)","five-business-day liquidity (90% limit)","annual turnover (25% limit)","calendar-year loss limit (10%; definition unresolved)","rolling five-year CPI+4% objective"]
    return {"verdict":"FAIL—coded checks" if fails else "PASS—coded checks only","checks":checks,"unverified":unverified}
