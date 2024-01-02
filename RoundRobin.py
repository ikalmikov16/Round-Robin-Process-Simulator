# Round Robin Simulator
# Calculates Completion Times
# Then Calls for functions to calculate turnaround and waiting times
def round_robin_sim(processes : list, quantum : int, context_switch : int) -> None:

    # Initialize vairables
    # Current time tracker
    current_time = 0
    # boolean used to track completion of processes
    completed = False
    # burst time left for each process stored in an array 
    burst_time_left = []
    for p in processes:
        burst_time_left.append(p.burst_time)
    
    # Display Beginning of Gantt Chart
    print("-------- Gantt Chart --------")

    # Simlate Round Robin and Calculate Completion Times
    # While All processes are not completed 
    while(not completed):
        completed = True

        # Iterate through each process and burst time left
        for i, p in enumerate(processes):
            if burst_time_left[i] > 0:
                # If process has arrived 
                if p.arrival_time <= current_time:
                    if burst_time_left[i] > quantum:
                        display_gantt_chart(p.pid, current_time, quantum, context_switch)

                        # Mark Processes as incomplete
                        completed = False
                        # Update current time and burst time left
                        current_time += quantum + context_switch
                        burst_time_left[i] -= quantum
                    else:
                        display_gantt_chart(p.pid, current_time, burst_time_left[i], context_switch)

                        # Update current timeand burst time left
                        current_time += burst_time_left[i] + context_switch
                        burst_time_left[i] = 0
                        # Store process completion time
                        p.completion_time = current_time - context_switch

                # If process has not arrived we can break the loop
                # because processes are sorted by arrival time
                else:
                    break
        
        # If processes are not completed due to current time not reaching the process's arrival time
        if completed:
            for p in processes:
                if p.completion_time == -1:
                    completed = False
                    
                    # Update current time to the process arrival time
                    current_time = p.arrival_time
                    break

    # Display End of The Gantt Chart
    print("\n-------- Processes Completed --------\n\n")

    # Calculate Turnaround and Waiting Times
    get_turnaround_times(processes)
    get_waiting_times(processes)

    pass

def display_gantt_chart(pid, current_time, quantum, context_switch) -> None:
    time = current_time
    print(f"---------------------- {time} ms")

    time += quantum
    print(f"\nRunning Process #{pid}\n")
    print(f"---------------------- {time} ms")

    time += context_switch
    print( "Context Switch")
    # print(f"---------------------- {time} ms")

    pass

# Calculate Turnaround Times
# Turnaround time = completion time - arrival time
def get_turnaround_times(processes) -> None:
    for p in processes:
        p.turnaround_time = p.completion_time - p.arrival_time
    pass

# Calculate Waiting Times
# Waiting time = turnaround time - burst time
def get_waiting_times(processes) -> None:
    for p in processes:
        p.waiting_time = p.turnaround_time - p.burst_time
    pass

# Calculate Avergae Turnaround and Waiting Times
# Store in arr = [Avg turnaround, Avg waiting]
# Return the array and store in an array to simplify final result display
def get_average_times(processes) -> list:
    arr = [0, 0]
    for p in processes:
        arr[0] += p.turnaround_time
        arr[1] += p.waiting_time
    arr[0] /= len(processes)
    arr[1] /= len(processes)

    return arr