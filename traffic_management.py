import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

# Demonstration map coordinates (abstract grid, not real geographic coordinates)
hospitals = pd.DataFrame({
    "hospital": ["Hospital A", "Hospital B", "Hospital C"],
    "x": [8, 2, 9],
    "y": [8, 9, 2]
})

accident = np.array([4.0, 3.0])
emergency_vehicle = np.array([3.0, 3.5])

# Select nearest hospital to the emergency location
hospitals["distance"] = np.sqrt(
    (hospitals["x"] - accident[0]) ** 2 +
    (hospitals["y"] - accident[1]) ** 2
)

nearest = hospitals.loc[hospitals["distance"].idxmin()]

# Create a simple corridor of intersections between vehicle and hospital
hospital_point = np.array([nearest["x"], nearest["y"]])
steps = 5

corridor = np.column_stack([
    np.linspace(emergency_vehicle[0], hospital_point[0], steps),
    np.linspace(emergency_vehicle[1], hospital_point[1], steps)
])

signals = pd.DataFrame({
    "intersection": [f"Signal {i+1}" for i in range(steps)],
    "priority": ["EMERGENCY PRIORITY"] * steps,
    "green_time_seconds": [90, 80, 70, 60, 50]
})

print("Nearest hospital:", nearest["hospital"])
print(f"Distance: {nearest['distance']:.2f} grid units")
print("\nPriority corridor:")
print(signals.to_string(index=False))

# Visualization
plt.figure(figsize=(8, 6))
plt.scatter(hospitals["x"], hospitals["y"], s=100, label="Hospitals")
plt.scatter(*accident, marker="X", s=140, label="Emergency Location")
plt.scatter(*emergency_vehicle, marker="o", s=100, label="Emergency Vehicle")
plt.plot(corridor[:, 0], corridor[:, 1], linewidth=2, label="Priority Corridor")

for i, point in enumerate(corridor):
    plt.scatter(point[0], point[1], marker="s", s=70)
    plt.text(point[0] + 0.1, point[1] + 0.1, f"S{i+1}")

plt.xlabel("X Coordinate (simulation)")
plt.ylabel("Y Coordinate (simulation)")
plt.title("Emergency-Aware Signal Priority Simulation")
plt.legend()
plt.tight_layout()
plt.savefig("results/signal_priority.png", dpi=200)
plt.close()
