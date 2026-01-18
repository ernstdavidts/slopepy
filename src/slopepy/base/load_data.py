from numpy.typing import ArrayLike
import numpy as np
import pandas as pd
from dataclasses import dataclass
import numpy as np
from pathlib import Path


@dataclass
class TestData:
    x: np.ndarray # intensiteit
    y: np.ndarray # zuurstofopname

def load_data(source: str, intensity: ArrayLike = "Watt", parameter: ArrayLike = "V'CO2", warm_up: int = 3, sampling_rate: int = 12):
    protocol = warm_up * sampling_rate
    if isinstance(source, pd.DataFrame):
        df = source
    
    else: 
        source = Path(source)

        if source.suffix.lower() == ".csv":
            df = pd.read_csv(source, skiprows=[1])
        elif source.suffix.lower() in {".xls", ".xlsx"}:
            df = pd.read_excel(source, skiprows=[1])
        
        else:
            raise ValueError(f"Onbekend bestandtype: {source.endswith}")

    x = df[intensity].to_numpy().astype(float)
    y = df[parameter].to_numpy().astype(float)
    
    return x, y
      

if __name__ == "__main__":
    x, y = load_data("/Users/ernstdavidts/slopepy/slopepy/tests/test/test_data/RAMP 17.11.xlsx", "WR", "V'CO2")
    print(x)
    print(y)