# Irakli Kalmikov
# Operating Systems
# Professor Dent
# Round Robin Process Scheduler Simulator - Final Project
# This program takes user input to gather information about the scheduler and processes and Simulates the Round Robin
# It displays a Gantt Chart as it simulates through the processes
# It displays information about each process with their Completion, Turnaround, and Waiting Times
# It displays Average Turnaround and Waiting Times

from RoundRobin import *
from Process import Process
from tabulate import tabulate

print("\n\nWelcome to the Round Robin Simulator!!\n\n")

# Initialize Variables

# Gather User input for number of processes
# Store all processes in an array
n = int(input("Enter the number of Processes: "))
processes = []

# Gather User input for quantum and context switch times
# Stored as ints for simplicity
quantum = int(input("Enter the Quantum time(ms): "))
context_switch = int(input("Enter the Context-Switch time(ms): "))

# Table Array to display final results 
table_array = [["Process", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]]
average_times = [["Average Turnaround Time", "Average Waiting Time"]]

# Gather User input for process details
print("\n\nNow let's enter some process details!\n")

for i in range(n):
    pid = i+1
    print(f"Process #{pid}")
    burst_time = int(input("Enter the Burst time(ms): "))
    arrival_time = int(input("Enter the Arrival time(ms): "))
    print("\n")

    # Sort processes by arrival time in the processes array
    j = 0
    for p in processes:
        if arrival_time < p.arrival_time:
            break
        j += 1
    processes = processes[:j] + [Process(pid, burst_time, arrival_time)] + processes[j:]


# Simulate Round Robin and calculate completion, turnaround, and waiting times
round_robin_sim(processes, quantum, context_switch)
average_times.append(get_average_times(processes))


# Update Table array with final results
for p in processes:
    table_array.append([p.pid, p.arrival_time, p.burst_time, p.completion_time, p.turnaround_time, p.waiting_time])

# Display Final Results
# Quantum Time and Context Switch time 
print(tabulate([[f"Quantum Time = {quantum} ms"], [f"Context Switch Time = {context_switch} ms"]], tablefmt = "fancy_grid"))
# Final Process Results
print(tabulate(table_array, headers = "firstrow", tablefmt = "fancy_grid"))
# Average Turnaround and Waiting Times
print(tabulate(average_times, headers = "firstrow", tablefmt = "fancy_grid"))