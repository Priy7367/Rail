import datetime

class TrainLogger:
    def __init__(self, log_file="train_schedule.log"):
        self.log_file = log_file

    def log_event(self, event_type, message):
        """
        Log actions with timestamps.
        
        :param event_type: Type of the event (e.g., "INFO", "ERROR")
        :param message: The message to log
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} [{event_type}] {message}\n"
        
        with open(self.log_file, 'a') as file:
            file.write(log_entry)

    def generate_report(self):
        """
        Create summary report.
        """
        with open(self.log_file, 'r') as file:
            lines = file.readlines()
        
        report = []
        for line in lines:
            timestamp, event_type, message = line.strip().split('] ', 2)
            event_type = event_type[1:]  # Remove leading '['
            report.append((timestamp, event_type, message))
        
        # Print or save the report
        for entry in report:
            print(f"Timestamp: {entry[0]}, Event Type: {entry[1]}, Message: {entry[2]}")

# Example usage
if __name__ == "__main__":
    logger = TrainLogger()
    
    logger.log_event("INFO", "Train A scheduled from Station A to Station G")
    logger.log_event("ERROR", "Train B failed to start at Station C")
    logger.log_event("INFO", "Train C re-routed from Station D to Station F")
    
    logger.generate_report()