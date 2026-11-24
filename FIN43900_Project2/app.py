"""FIN 43900 Project 2: Investment Committee Portfolio decision app."""
from datetime import date
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
from portfolio_core import (annualized_stats, max_drawdown, portfolio_metrics,
                           momentum_12_1, optimize_min_vol, mandate_verdict)

st.set_page_config(page_title="Investment Committee Portfolio | Project 2", layout="wide")
st.title("Investment Committee Portfolio — Investment Decision Application")
st.caption("Course demonstration. Historical estimates are uncertain and are not forecasts or investment advice.")

ASSETS={"Treasury bills / reserve":"SGOV", "Treasury 10-year proxy":"IEF", "Investment-grade bonds":"AGG", "Global equities":"ACWI"}
RISK_ASSETS=list(ASSETS.keys())[1:]
BENCHMARK=pd.Series({"Treasury bills / reserve":0.0,"Treasury 10-year proxy":0.0,"Investment-grade bonds":0.40,"Global equities":0.60})

@st.cache_data(ttl=3600, show_spinner="Downloading price history…")
def get_prices(start, end_exclusive):
    symbols=list(ASSETS.values())
    raw=yf.download(symbols,start=start,end=end_exclusive,auto_adjust=True,progress=False,group_by="column")
    if raw is None or raw.empty: raise ValueError("Price download returned no rows. Check connection, tickers, and dates.")
    close=raw["Close"] if isinstance(raw.columns,pd.MultiIndex) else raw[["Close"]].rename(columns={"Close":symbols[0]})
    close=close.rename(columns={ticker:name for name,ticker in ASSETS.items()})
    close=close.reindex(columns=list(ASSETS)).sort_index().ffill().dropna()
    if close.shape[0]<260: raise ValueError("Less than approximately one year of daily data is available.")
    return close


with st.sidebar:
    st.header("Run controls")
    asof=st.date_input("Decision / data cutoff",date.today())
    history_start=st.date_input("History start",date(2015,1,1))
    estimation_years=st.slider("Estimation window (years)",3,10,5)
    signal_months=st.select_slider("Momentum lookback (months; skips latest month)",[6,9,12],value=12)
    hurdle=st.slider("Estimated annual return hurdle (%)",0.0,15.0,6.5,0.25)/100
    reserve_min=st.slider("Reserve minimum (%)",3,20,3,1)/100
    cost_bps=st.slider("One-way implementation cost (bps)",0,100,10,5)
    stress_return_shift=st.slider("Stress: shift annual return estimates (percentage points)",-5.0,5.0,0.0,0.5)/100
    st.caption("Inputs are stress controls. The return hurdle is not a forecast or a guarantee.")

st.info("**Mandate summary:** $100m reserve; $750,000 quarterly payout; CPI + 4% over rolling five-year periods; 7-year horizon; 60/40 reference benchmark. Lab 13 constraints are carried forward, but several are not fully measurable in this prototype.")
if history_start>=asof:
    st.error("History start must be earlier than the cutoff.")
    st.stop()
try:
    end_exclusive=(pd.Timestamp(asof)+pd.Timedelta(days=1)).strftime("%Y-%m-%d")
    daily=get_prices(history_start.isoformat(),end_exclusive)
    daily=daily.loc[daily.index<=pd.Timestamp(asof)]
    month_prices=daily.resample("ME").last().dropna()
    # Exclude incomplete month-end from monthly signal/return series.
    latest_month_end=pd.Timestamp(asof).to_period("M").to_timestamp("M")
    if pd.Timestamp(asof).date()<latest_month_end.date(): latest_month_end-=pd.offsets.MonthEnd(1)
    month_prices=month_prices.loc[month_prices.index<=latest_month_end]
    monthly_returns=month_prices.pct_change().dropna()
    if len(monthly_returns)<36: st.error("At least 36 monthly return observations are required."); st.stop()
    estimation=monthly_returns.tail(estimation_years*12)
    expected=estimation.mean()*12+stress_return_shift
    covariance=estimation.cov()*12
    signal=momentum_12_1(month_prices,signal_months)
    st.subheader("1 — Data status and point-in-time signal")
    a,b,c=st.columns(3); a.metric("Last daily price date",daily.index.max().date().isoformat()); b.metric("Monthly return observations",len(monthly_returns)); c.metric("As-of cutoff",asof.isoformat())
    st.write("**Momentum signal:** cumulative price return over the chosen lookback, ending one full month before the cutoff. The signal ranks risk sleeves; it is not presented as proven alpha.")
    st.dataframe(signal.to_frame("Momentum signal").style.format("{:.2%}"),use_container_width=True)
    selected=signal.loc[RISK_ASSETS].sort_values(ascending=False).head(2).index.tolist()
    st.write("Selected risk sleeves:",", ".join(selected))
    # Baseline 1 equal weight, baseline 2 inverse-volatility; benchmark is displayed as context.
    equal=pd.Series(0.25,index=list(ASSETS))
    vol=estimation.std(ddof=1)*np.sqrt(12)
    inv=pd.Series(0.0,index=list(ASSETS)); inv[RISK_ASSETS]=1/vol[RISK_ASSETS].replace(0,np.nan)
    inv=inv.fillna(0); inv=inv/inv.sum()
    # Constrained portfolio: reserve bills plus the top two momentum risk sleeves; min-vol feasible grid.
    selected_assets=["Treasury bills / reserve"]+selected
    selected_expected=expected[selected_assets]
    selected_cov=covariance.loc[selected_assets,selected_assets]
    optimized=optimize_min_vol(selected_expected,selected_cov,{"Treasury bills / reserve"},reserve_min,hurdle,step=0.05)
    constrained=pd.Series(0.0,index=list(ASSETS))
    if optimized is not None: constrained.loc[optimized["weights"].index]=optimized["weights"]
    portfolios={"Equal weight baseline":equal,"Inverse-volatility baseline":inv}
    if optimized is not None:
        portfolios["Constrained momentum portfolio"]=constrained
    st.subheader("2 — Allocations")
    alloc=pd.DataFrame(portfolios)*100
    st.dataframe(alloc.style.format("{:.1f}%"),use_container_width=True)
    st.bar_chart(alloc)
    st.subheader("3 — Performance and risk comparison")
    rows=[]; histories={}
    for name,w in portfolios.items():
        metrics=portfolio_metrics(w,monthly_returns.tail(estimation_years*12),cost_bps)
        histories[name]=metrics["returns"]
        rows.append({"Portfolio":name,"Annualized historical return":metrics["annualized_return"],"Annualized volatility":metrics["annualized_volatility"],"Max drawdown":metrics["max_drawdown"],"Reserve weight":w.get("Treasury bills / reserve",0)})
    st.dataframe(pd.DataFrame(rows).set_index("Portfolio").style.format("{:.2%}"),use_container_width=True)
    wealth=pd.DataFrame({k:(1+v.fillna(0)).cumprod() for k,v in histories.items()})
    st.line_chart(wealth)
    st.subheader("4 — Mandate verdicts")
    verdict_rows=[]
    for name,w in portfolios.items():
        v=mandate_verdict(w,reserve_min)
        verdict_rows.append({"Portfolio":name,"Verdict":v["verdict"],"Rule results": "; ".join(v["checks"]),"Unverified hard rules":v["unverified"]})
    st.dataframe(pd.DataFrame(verdict_rows),use_container_width=True)
    st.warning("Conservative interpretation: an overall mandate PASS is not awarded because ETF look-through issuer concentration, 5-business-day liquidity, annual turnover, and the 10% calendar-year loss rule are not fully verified. These are reported as unverified rather than assumed compliant.")
    st.subheader("5 — Stress run and stop condition")
    st.write(f"Stress inputs currently applied: return-estimate shift **{stress_return_shift:+.1%}**; estimation window **{estimation_years} years**; one-way trading-cost estimate **{cost_bps} bps**; reserve floor **{reserve_min:.0%}**; annual hurdle **{hurdle:.1%}**.")
    if optimized is None:
        st.error("STOP CONDITION TRIGGERED: no feasible portfolio satisfies the selected return hurdle and reserve floor. Do not force an allocation or relax hard constraints automatically.")
    elif any(mandate_verdict(w,reserve_min)["verdict"]!="PASS—coded checks only" for w in portfolios.values()):
        st.warning("STOP / REVIEW: at least one coded rule failed. Do not recommend that portfolio without reviewing the failed rule.")
    else:
        st.success("No coded allocation rule failed. This is not a full mandate pass because several hard rules remain unverified.")
    st.caption("Use the controls to repeat the stress run with a different estimation window, return shift, hurdle, cost, and reserve floor. Record inputs, prediction, output, and decision impact.")
    st.subheader("6 — Recommendation")
    st.write("**Preliminary recommendation: PILOT / DEFER FULL ADOPTION.** The signal is simple and transparent but not demonstrated to deliver alpha. Historical sample estimates are unstable, and mandate rules remain partly unverified.")
    st.write("**Illustrative pilot range:** 0–10% of reserve assets, only after committee approval, data verification, and completion of mandate checks. This range is a project judgment—not an optimizer output.")
    st.write("**Monitoring / reversal triggers:** point-in-time data cannot be reproduced; reserve or liquidity requirement is breached; a hard mandate rule fails; optimizer becomes infeasible; allocations change materially under small assumption/window changes; or actual costs exceed the stress assumption.")
    st.subheader("7 — Data export")
    if st.button("Save downloaded daily prices to data/prices.csv"):
        daily.to_csv("data/prices.csv")
        st.success("Saved data/prices.csv. Commit only if the project submission permits the dataset and licensing terms.")
except Exception as exc:
    st.error(f"Application run failed: {exc}")
    st.caption("Check network access, Yahoo Finance availability, package installation, ticker data, and selected dates. A failure is not a portfolio result.")
