# Project Title

A dynamic, intelligent train scheduling system that leverages backtracking to optimize train routes between two stations, addressing real-time traffic, congestion, and safety constraints.

## Table of Contents

   . Project Description

   . Features

   . Getting Started

       . Prerequisites

        .Installation

   . Usage

   . License

   . Contact

## Project Description

The Intelligent Train Scheduling System (ITSS) is designed to dynamically optimize train routes from a source to a destination station through intermediate stations using a backtracking-based algorithm. It aims to:

    Minimize delays

    Avoid route conflicts

    Ensure compliance with safety standards

    Provide optimal and adaptive routing even under congestion or emergency conditions

The system operates through real-time monitoring, conflict detection, and rollback strategies, making it ideal for highly congested or dynamic railway networks.

## Features

    🚆 Dynamic Route Planning: Adapts routes in real-time based on traffic and operational changes.

    🔄 Backtracking Algorithm: Handles congestion by retreating and rescheduling intelligently.

    🛡️ Safety Protocol Compliance: Enforces safety rules and handles emergencies.

    ⚡ Multi-Objective Optimization: Considers travel time, safety, passenger comfort, and resource efficiency.

    📈 Performance Reporting: Generates logs and delay analytics.

    🔧 Scalable Design: Easily extendable for multi-train and multi-route systems.



## Getting Started

### Prerequisites

   . Python 3.8+

   . pandas

   . networkx

   . matplotlib (optional for visualization)

   . VS Code or any IDE for Python development
   
### Installation

A step-by-step series of examples the have the development environment running:

1. Clone the repository:
   ```bash
   git clone https://github.com/Priy7367/intelligent-train-scheduler.git


   cd yourproject
   intelligent-train-scheduler

## Usage

You can run the project by executing:
```bash
python main.py

This will:

    Build the train network graph

    Monitor real-time traffic

    Use backtracking in case of congestion

    Print final optimized route with logs
  Example
    T+0: Departed Source
    T+60: Arrived Station_A
    T+60: ⚠ High traffic detected at Station_B
    T+60: 🔄 Backtracking activated
    T+90: ✅ Resuming journey
    T+150: Arrived Station_B
    T+210: Arrived Destination

## Licence

This project is licensed under the MIT License — see the LICENSE file for details.

## Contact

Project Owner: Priyranjan Raj
Email: priyranjanraj108@outlook.com
LinkedIn/GitHub: Priy7367
   
