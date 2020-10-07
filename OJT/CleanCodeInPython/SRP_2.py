"""
    Make the SystemMonitor class more smaller
"""

class AlertSystem:
    def __init__(self, activityReader, systemMonitor, output):
        self.activityReader = activityReader
        self.systemMonitor = systemMonitor
        self.output = output

    def run(self):
        self.activityReader.load()
        self.systemMonitor.identify_event()
        self.output.stream()
    
class ActivityReader:
    def __init__(self, name):
        self.name = name

    def load(self):
        print("Activity Reader: Load ", self.name)

class SystemMonitor:
    def __init__(self) -> None:
        self.thread_hold = 0

    def identify_event(self):
        print("System Monitor identify event ", self.thread_hold)

class Output:
    def __init__(self) -> None:
        self.hello = 'hello'

    def stream(self):
        print("Output stream")
        print(self.hello)

alertSystem = AlertSystem(ActivityReader('bao'), SystemMonitor(), Output())
alertSystem.run()