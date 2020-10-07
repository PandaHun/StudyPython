"""
    A class has many responsibilities
    This SystemMonitor class a set ot method that are orthogonal
    each one can be done indepedently of the rest
"""

class SystemMonitor:
    def load_activity(self):
        """Get the events from a source"""
        print("1. Load activity")

    def identify_events(self):
        """Parse the source raw data into events"""
        print("2. Identify events")

    def stream_events(self):
        """Send the parsed events to an external agent"""
        print("3. Stream event")

"""
    If any of this change, the SystemMonitor class will need to change
    There are lots of differents reasons that will impact on changes in this class
    So, solution is to create smaller and more cohesive abstractions
"""