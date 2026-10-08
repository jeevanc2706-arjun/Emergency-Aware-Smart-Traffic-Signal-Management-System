```python
import numpy as np
import pandas as pd


def find_nearest_hospital(hospitals, accident):
    distances = np.sqrt(
        (hospitals["x"] - accident[0]) ** 2
        + (hospitals["y"] - accident[1]) ** 2
    )

    hospitals = hospitals.copy()
    hospitals["distance"] = distances

    return hospitals.loc[hospitals["distance"].idxmin()]


def test_nearest_hospital():
    hospitals = pd.DataFrame({
        "hospital": ["A", "B", "C"],
        "x": [8.0, 2.0, 9.0],
        "y": [8.0, 9.0, 2.0]
    })

    accident = np.array([4.0, 3.0])

    nearest = find_nearest_hospital(
        hospitals,
        accident
    )

    assert nearest["hospital"] == "B"


def test_distance_is_non_negative():
    hospitals = pd.DataFrame({
        "hospital": ["A"],
        "x": [5.0],
        "y": [5.0]
    })

    accident = np.array([4.0, 3.0])

    nearest = find_nearest_hospital(
        hospitals,
        accident
    )

    assert nearest["distance"] >= 0
```
