import sys
sys.path.insert(0, "/Users/ernstdavidts/slopepy/slopepy/src")

from slopepy.base.load_data import load_data
from slopepy.base.analyzer import SlopeProtocolAnalyzer

print("Loading data...")
x, y = load_data(
    source= "/Users/ernstdavidts/slopepy/slopepy/tests/test/test_data/RAMP 17.11.xlsx",
    intensity="WR",
    parameter="V'CO2",
)
print(f"Data loaded: x shape {x.shape}, y shape {y.shape}")

print("Creating analyzer...")
analyzer = SlopeProtocolAnalyzer(
    x=x,
    y=y,
    baseline_watt=50
)

print("Running analysis...")
result = analyzer.analyze()
