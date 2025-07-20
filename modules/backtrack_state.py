import heapq
from datetime import datetime, timedelta

class BacktrackState:
    def __init__(self, graph, source, destination, train_type, start_time):
        self.graph = graph
        self.source = source
        self.destination = destination
        self.train_type = train_type
        self.start_time = start_time
        self.schedule = []
        self.conflicts = []

    def schedule_train(self):
        # Initialize the priority queue with the starting node
        pq = [(0, self.source, self.start_time)]
        visited = set()
        
        while pq:
            cost, current_node, current_time = heapq.heappop(pq)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            self.schedule.append((current_node, current_time))
            
            if current_node == self.destination:
                return True
            
            for neighbor, travel_time in self.graph[current_node].items():
                if neighbor not in visited:
                    new_time = current_time + timedelta(minutes=travel_time)
                    if not self.has_conflict(neighbor, new_time):
                        heapq.heappush(pq, (cost + travel_time, neighbor, new_time))
                    else:
                        self.conflicts.append((neighbor, new_time))
        
        return False

    def has_conflict(self, node, time):
        for scheduled_node, scheduled_time in self.schedule:
            if scheduled_node == node and abs((scheduled_time - time).total_seconds()) < 3600:  # 1 hour window
                return True
        return False

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 30, 'C': 45},
        'B': {'D': 20, 'E': 35},
        'C': {'D': 25, 'F': 40},
        'D': {'G': 15},
        'E': {'G': 20},
        'F': {'G': 25}
    }