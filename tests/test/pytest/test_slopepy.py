import numpy as np
from lactopy import SlopeProtocolAnalyzer

def test_vco2_mrt_correction_applied():
    analyzer = SlopeProtocolAnalyzer(
        data_path="tests/test_data/vco2_ramp_test.csv",
        intensity_column="WR",
        parameter_column="VCO2",
        warm_up_time=0,
        baseline_watt=50,
    )

    results = analyzer.analyze()

    assert results["breakpoint1"] != results["breakpoint1_raw"]
    assert results["breakpoint2"] != results["breakpoint2_raw"]
    assert results["breakpoint1"] < results["breakpoint2"]