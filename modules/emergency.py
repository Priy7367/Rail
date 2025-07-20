class EmergencyHandler:
    @staticmethod
    def handle_obstruction(train, location):
        """
        Implement obstruction protocol.
        
        :param train: The train object
        :param location: The location of the obstruction
        """
        print(f"Handling obstruction for train {train.id} at location {location}")
        # Example actions:
        # 1. Stop the train immediately
        train.stop()
        # 2. Notify the control center
        EmergencyHandler.notify_control_center(train, location)
        # 3. Re-route the train if possible
        EmergencyHandler.re_route_train(train, location)

    @staticmethod
    def handle_signal_failure(train, section):
        """
        Implement signal failure protocol.
        
        :param train: The train object
        :param section: The section where the signal failure occurred
        """
        print(f"Handling signal failure for train {train.id} in section {section}")
        # Example actions:
        # 1. Stop the train immediately
        train.stop()
        # 2. Notify the control center
        EmergencyHandler.notify_control_center(train, section)
        # 3. Re-route the train if possible
        EmergencyHandler.re_route_train(train, section)

    @staticmethod
    def notify_control_center(train, location_or_section):
        """
        Notify the control center about the emergency.
        
        :param train: The train object
        :param location_or_section: The location or section of the emergency
        """
        print(f"Notifying control center about emergency for train {train.id} at {location_or_section}")

    @staticmethod
    def re_route_train(train, location_or_section):
        """
        Re-route the train if possible.
        
        :param train: The train object
        :param location_or_section: The location or section of the emergency
        """
        print(f"Re-routing train {train.id} to avoid {location_or_section}")

# Example usage
if __name__ == "__main__":
    class Train:
        def __init__(self, id):
            self.id = id

        def stop(self):
            print(f"Train {self.id} stopped")

    train = Train(id=1)
    EmergencyHandler.handle_obstruction(train, "Station A")
    EmergencyHandler.handle_signal_failure(train, "Section 1")