# Process class to store individual processes
# pid = int (1 to n)
class Process:
    def __init__(self, pid : int, burst_time : int, arrival_time : int):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time

        # Initialize to -1 to signify incomplete
        self.completion_time = -1
        self.turnaround_time = -1
        self.waiting_time = -1
