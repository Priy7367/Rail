import matplotlib.pyplot as plt
import networkx as nx
import datetime

def plot_route(graph, path):
    """
    Visualize route using matplotlib/networkx.
    
    :param graph: The graph representing the railway network
    :param path: The list of nodes representing the route
    """
    G = nx.Graph()
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
    
    for node, time, speed, distance in schedule:
        distances.append(distance)
        speeds.append(speed)
    
    plt.figure(figsize=(10, 6))
    plt.plot(distances, speeds, marker='o', linestyle='-')
    plt.xlabel("Distance (km)")
    plt.ylabel("Speed (km/h)")
    plt.title("Speed vs Distance Profile")
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': {'distance': 30, 'max_speed': 130, 'traffic_profile': 'low'}},
        'B': {'C': {'distance': 45, 'max_speed': 130, 'traffic_profile': 'low'}},
        'C': {'D': {'distance': 60, 'max_speed': 130, 'traffic_profile': 'low'}}
    }
    
    path = ['A', 'B', 'C', 'D']
    plot_route(graph, path)
    
    schedule = [
        ('A', datetime.datetime(2023, 10, 2, 8, 0), 130, 0),
        ('B', datetime.datetime(2023, 10, 2, 8, 30), 130, 30),
        ('C', datetime.datetime(2023, 10, 2, 9, 0), 130, 75),
        ('D', datetime.datetime(2023, 10, 2, 9, 30), 130, 135)
    ]
    plot_speed_profile(schedule)