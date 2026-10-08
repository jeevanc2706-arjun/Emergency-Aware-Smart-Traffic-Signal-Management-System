# 🚦 Emergency-Aware Smart Traffic Signal Management System

A Python-based simulation of an intelligent traffic management system that identifies the nearest hospital, generates an emergency priority corridor, and dynamically calculates traffic-signal green times for an emergency vehicle.

## 🎯 Problem Statement

Emergency vehicles such as ambulances can lose valuable time because of traffic congestion and fixed traffic-signal timings.

This project demonstrates how an intelligent traffic management system can prioritize an emergency vehicle's route toward the nearest hospital.

## 💡 Solution

The system simulates an emergency scenario and performs the following steps:

1. Defines the emergency location and emergency vehicle position.
2. Calculates the distance between the emergency location and available hospitals.
3. Identifies the nearest hospital.
4. Generates a priority corridor from the emergency vehicle toward the selected hospital.
5. Calculates the distance of each intersection from the emergency vehicle.
6. Dynamically assigns green-light durations based on intersection distance.
7. Generates a visualization of the emergency priority corridor.
8. Saves the signal-priority data as a CSV file.

## 🧠 System Architecture

```text
Emergency Scenario
       │
       ▼
Emergency Location
       │
       ▼
Hospital Distance Calculation
       │
       ▼
Nearest Hospital Selection
       │
       ▼
Priority Corridor Generation
       │
       ▼
Intersection Distance Calculation
       │
       ▼
Dynamic Green-Time Allocation
       │
       ├───────────────┐
       ▼               ▼
   CSV Results      Visualization
```

## 🚀 Key Features

- Nearest-hospital selection using Euclidean distance
- Emergency vehicle location simulation
- Priority corridor generation
- Dynamic traffic signal green-time calculation
- Intersection distance analysis
- CSV result generation
- Traffic-system visualization
- Reproducible Python implementation

## 🛠️ Technologies

- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Jupyter Notebook**

## 📁 Project Structure

```text
emergency-aware-smart-traffic/
│
├── .gitignore
├── README.md
├── requirements.txt
├── traffic_management.py
├── traffic_analysis.ipynb
│
└── results/
    ├── signal_priority.csv
    └── signal_priority.png
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jeevanc2706-arjun/emergency-aware-smart-traffic.git
```

Move into the project directory:

```bash
cd emergency-aware-smart-traffic
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Simulation

```bash
python traffic_management.py
```

The program generates:

```text
results/signal_priority.csv
results/signal_priority.png
```

## 📊 Output

The system produces a table containing:

- Intersection ID
- Emergency priority status
- Distance from emergency vehicle
- Calculated green-light duration

Example workflow:

```text
Emergency Vehicle
        ↓
Nearest Hospital
        ↓
Priority Corridor
        ↓
Signal 1 → Signal 2 → Signal 3 → Signal 4 → Signal 5
        ↓
Dynamic Green-Time Allocation
```

## 📈 Visualization

The simulation generates a map showing:

- 🏥 Hospital locations
- 🚑 Emergency vehicle
- ❌ Emergency/accident location
- 🚦 Priority intersections
- ➡️ Emergency priority corridor
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/676ed225-eded-4bbb-a20a-3f6664573986" />


<img width="768" height="512" alt="image" src="https://github.com/user-attachments/assets/45297308-cfb3-453c-828a-0e671525bf61" />


## 🔬 Current Implementation

This version is a **simulation-based prototype** using abstract X/Y coordinates rather than real geographic coordinates.

The current implementation focuses on demonstrating the traffic-prioritization algorithm and emergency-route logic.

## 🔮 Future Improvements

The system can be extended with:

- Real-time emergency vehicle detection using computer vision
- YOLO-based vehicle detection
- GPS-based emergency vehicle tracking
- Real road-network data
- OpenStreetMap integration
- Real-time traffic-density analysis
- Multi-intersection optimization
- ETA prediction
- IoT-enabled traffic signal control
- Cloud-based traffic monitoring

## 👨‍💻 Author

**Jeevan C**

BE Artificial Intelligence & Machine Learning

GitHub: [jeevanc2706-arjun](https://github.com/jeevanc2706-arjun)
