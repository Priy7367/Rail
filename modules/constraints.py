from datetime import datetime, timedelta

class SafetyConstraints:
    MIN_HEADWAY = 300  # 5 minutes between trains
    MAX_SPEED = 130     # km/h

    @classmethod
    def check_headway(cls, last_train_time):
        """
        Calculate time since last train and check if it meets the minimum headway constraint.
        
        :param last_train_time: The time of the last train (datetime object)
        :return: True if the headway is sufficient, False otherwise
        """
        current_time = datetime.now()
        time_since_last_train = (current_time - last_train_time).total_seconds() / 60  # Convert to minutes
        return time_since_last_train >= cls.MIN_HEADWAY

class TimingConstraints:
    MAX_DELAY = 180  # 3 hours max delay

    @classmethod
    def check_schedule_feasibility(cls, schedule):
        """
        Verify that the schedule meets the timing constraints.
        
        :param schedule: A list of tuples (node, time) representing the schedule
        :return: True if the schedule is feasible, False otherwise
        """
        for i in range(1, len(schedule)):
            previous_time = schedule[i-1][1]
            current_time = schedule[i][1]
            delay = (current_time - previous_time).total_seconds() / 60  # Convert to minutes
            if delay > cls.MAX_DELAY:
                return False
        return True

# Example usage
if __name__ == "__main__":
    # Example schedule
    schedule = [
        ('A', datetime.now()),
        ('B', datetime.now() + timedelta(minutes=30)),
        ('C', datetime.now() + timedelta(minutes=60)),
        ('D', datetime.now() + timedelta(minutes=90))
    ]

    # Check headway
    last_train_time = schedule[-1][1]
    headway_valid = SafetyConstraints.check_headway(last_train_time)
    print(f"Headway valid: {headway_valid}")

    # Check schedule feasibility
    schedule_feasible = TimingConstraints.check_schedule_feasibility(schedule)
    print(f"Schedule feasible: {schedule_feasible}")