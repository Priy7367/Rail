import datetime

class TrafficPredictor:
    def __init__(self, traffic_data):
        self.traffic_data = traffic_data

    def predict_congestion(self, section, time):
        """
        Predict traffic based on historical patterns.
        
        :param section: The track section to predict traffic for
        :param time: The time to predict traffic for (datetime object)
        :return: Predicted traffic level (e.g., "low", "medium", "high")
        """
        hour = time.hour
        day_of_week = time.weekday()
        
        if section in self.traffic_data:
            for entry in self.traffic_data[section]:
                if entry['hour'] == hour and entry['day_of_week'] == day_of_week:
                    return entry['traffic_level']
        
        return "unknown"

    def get_current_traffic(self, section, hour):
        """
        Return current traffic level.
        
        :param section: The track section to get traffic for
        :param hour: The hour of the day (0-23)
        :return: Current traffic level (e.g., "low", "medium", "high")
        """
        current_time = datetime.datetime.now()
        return self.predict_congestion(section, current_time)

# Example usage
if __name__ == "__main__":
    traffic_data = {
        'Section 1': [
            {'hour': 7, 'day_of_week': 0, 'traffic_level': 'high'},
            {'hour': 8, 'day_of_week': 0, 'traffic_level': 'high'},
            {'hour': 9, 'day_of_week': 0, 'traffic_level': 'medium'},
            {'hour': 10, 'day_of_week': 0, 'traffic_level': 'low'}
        ],
        'Section 2': [
            {'hour': 7, 'day_of_week': 0, 'traffic_level': 'medium'},
            {'hour': 8, 'day_of_week': 0, 'traffic_level': 'high'},
            {'hour': 9, 'day_of_week': 0, 'traffic_level': 'high'},
            {'hour': 10, 'day_of_week': 0, 'traffic_level': 'medium'}
        ]
    }

    predictor = TrafficPredictor(traffic_data)
    
    # Predict congestion at Section 1 at 8:00 AM on a Monday
    predicted_traffic = predictor.predict_congestion('Section 1', datetime.datetime(2023, 10, 2, 8, 0))
    print(f"Predicted traffic for Section 1 at 8:00 AM on a Monday: {predicted_traffic}")
    
    # Get current traffic for Section 2
    current_traffic = predictor.get_current_traffic('Section 2', datetime.datetime.now().hour)
    print(f"Current traffic for Section 2: {current_traffic}")