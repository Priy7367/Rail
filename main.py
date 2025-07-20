import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import datetime

# Add module path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.graph_builder import build_graph_from_howrah_csv
from modules.train_scheduler import TrainScheduler
from modules.traffic_monitor import TrafficMonitor

def get_train_type(frequency_file, source, destination):
    """Get train type based on source and destination stations"""
    try:
        df = pd.read_csv(frequency_file)
        # Find route that matches source-destination pair
        for _, row in df.iterrows():
            if (row['Station1'].lower() == source.lower() and
                row['Station2'].lower() == destination.lower()):
                # Check if it's a high-frequency route (Express)
                if sum(row[4:]) > 20:  # Sum of all hourly frequencies
                    return "Express"
        return "Passenger"
    except Exception as e:
        print(f"⚠️ Warning: Could not determine train type ({e})")
    return "Passenger"  # Default fallback

def plot_route(graph, path):
    """
    Visualize route using matplotlib/networkx.
    :param graph: The graph representing the railway network
    :param path: The list of nodes representing the route
    """
    G = nx.DiGraph()
    for node in graph:
        G.add_node(node)
        for neighbor, properties in graph[node].items():
            G.add_edge(node, neighbor, weight=properties['distance'])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    # Highlight the path
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
    plt.title("Railway Route Visualization")
    plt.show()

def plot_speed_profile(schedule):
    """
    Create speed vs distance chart.
    :param schedule: A list of tuples (node, time, speed, distance)
    """
    distances = []
    speeds = []
    total_distance = 0
    for node, time, speed, distance in schedule:
        total_distance += distance
        distances.append(total_distance)
        speeds.append(speed)
    
    plt.figure(figsize=(10, 6))
    plt.plot(distances, speeds, marker='o', linestyle='-')
    plt.xlabel("Distance (km)")
    plt.ylabel("Speed (km/h)")
    plt.title("Speed vs Distance Profile")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    graph = {
        'A': {'B': {'distance': 30, 'max_speed': 130, 'traffic_profile': 'low'}},
        'B': {'C': {'distance': 45, 'max_speed': 130, 'traffic_profile': 'low'}},
        'C': {'D': {'distance': 60, 'max_speed': 130, 'traffic_profile': 'low'}}
    }
    path = ['A', 'B', 'C', 'D']
    plot_route(graph, path)
    
    # Example schedule with varying speeds
    schedule = [
        ('A', datetime.datetime(2023, 10, 2, 8, 0), 130, 0),
        ('B', datetime.datetime(2023, 10, 2, 8, 30), 130, 30),
        ('C', datetime.datetime(2023, 10, 2, 9, 0), 130, 75),
        ('D', datetime.datetime(2023, 10, 2, 9, 30), 130, 135)
    ]
    
    # Calculate speeds for each section
    for i in range(1, len(schedule)):
        prev_time = schedule[i-1][1]
        curr_time = schedule[i][1]
        time_diff = (curr_time - prev_time).total_seconds() / 60  # in minutes
        distance = schedule[i][3] - schedule[i-1][3]
        speed = distance / (time_diff / 60)  # in km/h
        schedule[i] = (schedule[i][0], schedule[i][1], speed, schedule[i][3])
    
    plot_speed_profile(schedule)