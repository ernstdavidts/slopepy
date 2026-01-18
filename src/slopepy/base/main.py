import sys
sys.path.insert(0, "/Users/ernstdavidts/slopepy/slopepy/src")

from slopepy.base.load_data import load_data
from slopepy.base.analyzer import SlopeProtocolAnalyzer

x, y = load_data(
    source= "/Users/ernstdavidts/slopepy/slopepy/tests/tests/test_data/RAMP_1711_Python.csv",
    intensity="WR",
    parameter="V'CO2",
)

analyzer = SlopeProtocolAnalyzer(
    x=x,
    y=y,
    baseline_watt=50
)

result = analyzer.analyze()
