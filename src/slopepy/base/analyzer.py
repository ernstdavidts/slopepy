from dataclasses import dataclass
from typing import Iterable
import numpy as np
import pandas as pd
import piecewise_regression
from sklearn.linear_model import LinearRegression
from .load_data import load_data

x, y = load_data(
    source="/Users/ernstdavidts/slopepy/slopepy/tests/tests/test_data/RAMP_1711_Python.csv",
    intensity="WR",
    parameter="V'CO2",
)

@dataclass
class SlopeProtocolResults:
    breakpoint1: float
    breakpoint2: float
    breakpoint1_raw: float
    breakpoint2_raw: float
    mrt: float
    pw_fit: piecewise_regression.Fit

class SlopeProtocolAnalyzer:
    """
    Generieke hellingsprotocol-analyse voor ventilatoire parameters
    (bv. VE, VO2, VCO2, RER, etc.)
    """

    def __init__(
        self,
        x = np.ndarray,
        y = np.ndarray,
        baseline_watt:int = 50,
    ):
        self.x = x
        self.y = y
        self.baseline_watt = baseline_watt

    # -------------------------
    # Piecewise regression
    # -------------------------
    def compute_breakpoints(self):
        pw_fit = piecewise_regression.Fit(self.x, self.y, n_breakpoints=2)
        results = pw_fit.get_results()

        bp1 = results["estimates"]["breakpoint1"]["estimate"]
        bp2 = results["estimates"]["breakpoint2"]["estimate"]

        return bp1, bp2, pw_fit

    # -------------------------
    # correcties 
    # -------------------------
    def _compute_mrt(self):

        ybase = np.mean(self.y[:50])

        xregr = self.x[60:140]
        yregr = self.y[60:140]

        model = LinearRegression()
        model.fit(xregr.reshape(-1, 1), yregr)

        a = model.coef_[0]
        b = model.intercept_

        x_estimated = (ybase - b) / a
        mrt = x_estimated - self.baseline_watt

        return mrt

    # -------------------------
    # Volledige analyse
    # -------------------------
    def analyze(self) -> SlopeProtocolResults:
        bp1, bp2, pw_fit = self.compute_breakpoints()

        mrt = self._compute_mrt()
        bp1_corr = bp1 - mrt
        bp2_corr = bp2 - mrt
        bp2_corr = bp2_corr - ((bp2 - bp1) * (0.014 - 0.01) / 0.014)

        return SlopeProtocolResults(
            breakpoint1=bp1_corr,
            breakpoint2=bp2_corr,
            breakpoint1_raw=bp1,
            breakpoint2_raw=bp2,
            mrt=mrt,
            pw_fit=pw_fit
        )