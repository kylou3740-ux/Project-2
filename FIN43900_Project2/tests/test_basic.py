import unittest
import numpy as np
import pandas as pd
from portfolio_core import annualized_stats, max_drawdown, momentum_12_1, optimize_min_vol, mandate_verdict


class CoreTests(unittest.TestCase):
    def test_annualized_stats(self):
        r=pd.Series([.01,.02,-.01,.015])
        ann,vol=annualized_stats(r)
        self.assertAlmostEqual(ann,r.mean()*12)
        self.assertGreater(vol,0)
    def test_drawdown(self):
        self.assertLess(max_drawdown(pd.Series([.1,-.2,.05])),0)
    def test_momentum_skip_latest(self):
        idx=pd.date_range("2024-01-31",periods=15,freq="ME")
        p=pd.DataFrame({"A":np.arange(100,115)},index=idx)
        sig=momentum_12_1(p,12)
        self.assertAlmostEqual(sig["A"],p.iloc[-2]["A"]/p.iloc[2]["A"]-1)
    def test_optimizer_feasible_and_reserve(self):
        exp=pd.Series([.03,.08],index=["cash","risk"]); cov=pd.DataFrame([[.01,0],[0,.02]],index=exp.index,columns=exp.index)
        out=optimize_min_vol(exp,cov,{"cash"},.1,.04,step=.1)
        self.assertIsNotNone(out)
        self.assertGreaterEqual(out["weights"]["cash"],.1)
        self.assertAlmostEqual(out["weights"].sum(),1)
    def test_optimizer_infeasible(self):
        exp=pd.Series([.01,.02]); cov=pd.DataFrame(np.eye(2),index=exp.index,columns=exp.index)
        self.assertIsNone(optimize_min_vol(exp,cov,{"cash"},.1,.10))
    def test_mandate_reports_unverified(self):
        w=pd.Series({"Treasury bills / reserve":.03,"Treasury 10-year proxy":.2,"Investment-grade bonds":.3,"Global equities":.47})
        result=mandate_verdict(w,.03)
        self.assertTrue(result["verdict"].startswith("PASS"))
        self.assertGreater(len(result["unverified"]),0)
if __name__=="__main__": unittest.main()
