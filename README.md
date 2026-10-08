# 🚦 Emergency-Aware Smart Traffic Signal Management System

An AI-powered traffic management system designed to detect emergency vehicles and dynamically prioritize traffic signals to create a clear route toward the nearest hospital.

## 🎯 Problem Statement

Emergency vehicles such as ambulances and fire trucks can lose critical time because of traffic congestion and conventional fixed-time traffic signals.

This project aims to use **computer vision and intelligent traffic signal management** to identify emergency vehicles and provide them with priority at intersections.

## 💡 Proposed Solution

The system detects and tracks emergency vehicles, determines their movement through the traffic network, and dynamically prioritizes signals along the required route.

### System Workflow

```text
Traffic Camera
      ↓
Vehicle Detection
      ↓
Emergency Vehicle Identification
      ↓
Real-Time Tracking
      ↓
Route / Intersection Analysis
      ↓
Dynamic Signal Prioritization
      ↓
Priority Corridor
      ↓
Nearest Hospital
```

## 🚀 Key Features

- Emergency vehicle detection
- Real-time vehicle tracking
- Dynamic traffic signal prioritization
- Emergency priority corridor generation
- Accident-location based routing
- Nearest hospital coordination
- Automated traffic management logic

## 🛠️ Technologies

- Python
- OpenCV
- YOLO
- Computer Vision
- Machine Learning
- Traffic Signal Simulation

## 📁 Project Structure

```text
emergency-aware-smart-traffic/
│
├── src/
│   ├── detection.py
│   ├── tracking.py
│   ├── traffic_signal.py
│   └── main.py
│
├── models/
│   └── README.md
│
├── data/
│   └── README.md
│
├── tests/
│   └── test_system.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/jeevanc2706-arjun/emergency-aware-smart-traffic.git
cd emergency-aware-smart-traffic
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

```bash
python src/main.py
```

Follow the project configuration instructions to provide the required input video, model and traffic configuration.

## 📊 Results

For example:

- Emergency vehicle detection accuracy: not measured
- Vehicle tracking performance: demonstraded through vedio based tracking
- Signal response time: not quantitatively measured

## 📸 Demo

core functionalities:

* Vehicle Detection — Detects vehicles from the video feed.
* Emergency Vehicle Identification — Identifies and highlights emergency vehicles.
* Vehicle Tracking — Maintains vehicle tracking across video frames.
* Signal Prioritization — Prioritizes the traffic signal for an approaching emergency vehicle.
  <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d3d412b8-9bd9-4efc-a253-32c1b452f658" />


Note: Quantitative performance metrics were not recorded in the original project, so no estimated or fabricated accuracy, tracking, or response-time values are reported

## 🔮 Future Improvements

- GPS-based emergency vehicle tracking
- Integration with real traffic controllers
- Multi-intersection optimization
- Cloud-based traffic monitoring
- Edge deployment
- Emergency vehicle ETA prediction

## 👨‍💻 Author

**Jeevan C**

BE Artificial Intelligence & Machine Learning
