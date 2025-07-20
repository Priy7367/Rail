class SafetyManager:
    def __init__(self):
        # You can later add real-time safety logic here (weather, accidents etc.)
        self.safe_stations = ["Station_A", "Station_B", "Howrah", "Malda Town"]

    def get_nearest_safe_station(self, current_train_id: str) -> str:
        # In real use-case, you’ll calculate based on location of train_id
        print(f"🔒 [SafetyManager] Emergency triggered for Train {current_train_id}")
        return self.safe_stations[0]  # Always return a default safe station for now
