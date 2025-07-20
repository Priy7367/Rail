from typing import List, Dict, Any
import networkx as nx
import matplotlib.pyplot as plt

class TrainScheduler:
    def __init__(self, graph: Dict[str, Dict[str, Dict[str, Any]]], source: str, destination: str, train_type: str, start_time: str, constraints: Dict[str, Any] = None):
        """
        Initialize the train scheduler.
        Args:
            graph: Railway network graph
            source: Starting station
            destination: Ending station
            train_type: Type of train (Express/Passenger)
            start_time: Departure time (HH:MM format)
            constraints: Dictionary of scheduling constraints
        """
        self.graph = graph
        self.source = source
        self.destination = destination
        self.train_type = train_type
        self.start_time = start_time
        self.constraints = constraints or {}
        self.scheduled_path = None
        self.train_id = None
        self.traffic_monitor = TrafficMonitor()

    def schedule(self) -> Dict[str, Any]:
        """Schedule the train on the optimal path using backtracking and traffic data"""
        all_paths = []
        self.backtrack(self.source, [self.source], all_paths)
        
        if not all_paths:
            return {"status": "no_path", "message": "No route available"}
        
        # Calculate travel time for each path and adjust based on traffic
        best_path = None
        min_travel_time = float('inf')
        
        for path in all_paths:
            travel_time = self.calculate_travel_time(path)
            if travel_time < min_travel_time:
                min_travel_time = travel_time
                best_path = path
        
        if best_path is None:
            return {"status": "no_path", "message": "No valid route found"}
        
        total_distance = sum(
            self.graph[best_path[i]][best_path[i+1]]['distance']
            for i in range(len(best_path)-1)
        )
        
        self.scheduled_path = best_path
        return {
            "status": "scheduled",
            "path": best_path,
            "distance": total_distance,
            "estimated_time": f"{min_travel_time} minutes"
        }

    def backtrack(self, current_station: str, path: List[str], all_paths: List[List[str]]):
        """Backtracking search to find all paths from source to destination"""
        if current_station == self.destination:
            all_paths.append(path[:])
            return
        
        for neighbor in self.graph[current_station]:
            if neighbor not in path:  # Avoid cycles
                path.append(neighbor)
                self.backtrack(neighbor, path, all_paths)
                path.pop()

    def calculate_travel_time(self, path: List[str]) -> float:
        """Calculate the travel time for a given path considering traffic"""
        total_time = 0
        for i in range(len(path) - 1):
            distance = self.graph[path[i]][path[i+1]]['distance']
            max_speed = self.graph[path[i]][path[i+1]]['max_speed']
            traffic_level = self.traffic_monitor.get_current_traffic(path[i+1])
            
            # Adjust speed based on traffic level
            speed_factor = 1 - (traffic_level / 100)  # Simplified adjustment
            effective_speed = max_speed * speed_factor
            
            # Calculate time for this section
            time_for_section = (distance / effective_speed) * 60  # in minutes
            total_time += time_for_section
        
        return total_time

    def monitor_execution(self, train_id: str) -> Dict[str, Any]:
        """Monitor train execution status"""
        self.train_id = train_id
        # In a real system, this would connect to live tracking
        return {
            "train_id": train_id,
            "status": "on_time",
            "current_station": self.source,
            "progress": "0%"
        }

    def handle_emergency(self, train_id: str, emergency_type: str) -> Dict[str, Any]:
        """Handle emergency situations"""
        # In a real system, this would trigger specific protocols
        return {
            "train_id": train_id,
            "action": "halt_train",
            "message": f"Emergency protocol activated for {emergency_type}",
            "status": "halted"
        }

    def plot_routes(self, all_paths: List[List[str]], travel_times: List[float]):
        """Plot all possible routes and their travel times"""
        G = nx.DiGraph()
        for node in self.graph:
            G.add_node(node)
            for neighbor, properties in self.graph[node].items():
                G.add_edge(node, neighbor, weight=properties['distance'])
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
        
        for path, travel_time in zip(all_paths, travel_times):
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.5, edge_color='r')
            plt.text(pos[path[-1]][0], pos[path[-1]][1], f"Time: {travel_time:.2f} min", fontsize=9, ha='right')
        
        plt.title("Possible Routes and Travel Times")
        plt.show()