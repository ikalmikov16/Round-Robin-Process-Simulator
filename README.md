# Python Round Robin Process Scheduler Simulator

This project simulates a Round Robin Process Scheduler depending on the user input.
The user inputs the number of processes, quantum time, and context-switch time. 
Then user also inputs burst time and arrival time for each process. 

The program simulates the Round Robin Scheduler using the given processes.
As it completes each process it calculates the completion times.
With the completion times, it can calculate the turnaround and waiting times simply.

As it simulates, the program displays a Gantt Chart and marks the beginning and
end of each process quantum run and context-switch. 
Finally, the Program displays table lisiting each process with its arrival, burst, 
completion, turnaround, and waiting times. 
It also displays the average turnaround and waiting times.

## Installation Instructions for Users

* Download Python
* Download Python tabulate (used to display final results in a nice table)
* Execute main.py in Terminal
* For all inputs please use integers greater than -1 (Program does not account for input errors)
