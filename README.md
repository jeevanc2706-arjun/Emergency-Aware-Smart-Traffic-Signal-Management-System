# Emergency-Aware Smart Traffic Signal Management System

## Overview

A portfolio implementation of a smart traffic management concept that dynamically prioritizes emergency vehicles and creates a coordinated priority corridor toward a hospital.

The system models emergency-vehicle tracking, signal prioritization, and route-level coordination.

> **Reconstructed portfolio implementation:** The original source files and implementation were no longer available. This repository is reconstructed from the project description in my resume and should not be represented as the original source code.

## Core Idea

Accident / Emergency Location → Emergency Vehicle Tracking → Hospital Selection → Priority Corridor → Dynamic Signal Timing

## Features

- Emergency vehicle detection/tracking simulation
- Nearest-hospital selection from predefined locations
- Priority-corridor generation
- Dynamic traffic-signal timing
- Visualization of signal states

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib

## How to Run

```bash
pip install -r requirements.txt
python src/traffic_management.py
```

## Project Structure

```text
smart-traffic-signal-management/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── traffic_management.py
├── notebooks/
│   └── traffic_analysis.ipynb
└── results/
    └── signal_priority.png
```

## Limitations

This repository contains a simulation rather than a live traffic-control system. It does not connect to real emergency vehicles, hospital systems, GPS services, or physical traffic signals.

## Author

Jeevan C
