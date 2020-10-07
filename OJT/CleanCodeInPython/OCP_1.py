"""
    A class maintainability perils for not following the OCP
"""


class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def run(self):
        print(self.raw_data)


class UnknownEvent(Event):
    def do(self):
        print("Unkwon Event")


class LoginEvent(Event):
    def do(self):
        print("login")


class LogoutEvent(Event):
    def do(self):
        print("logout")


class SystemMonitor:
    """Identify events that occurred in the system."""
    def __init__(self, event_data):
        self.event_data = event_data
    
    def identify_event(self):
        if (
            self.event_data["before"]["session"] == 0
            and self.event_data["after"]["session"] == 1
        ):
            return LoginEvent(self.event_data)
        elif (
            self.event_data["before"]["session"] == 1
            and self.event_data["after"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)

l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
print(l1.identify_event().__class__.__name__)

l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
print(l2.identify_event().__class__.__name__)

"""
    the logic for determinig the types of events is centralized inside a monolithic method
    if number of events grow up, it could being a very long method, which is bad
    Every time we want to add new type of event to the system, have to change in this method
"""