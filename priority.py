# CPU Scheduling - Priority Scheduling (Non-preemptive)

def find_waiting_time(processes, n, bt, wt, priority):
    # Sort processes by priority (lower number = higher priority)
    sorted_processes = sorted(zip(processes, bt, priority), key=lambda x: x[2])
    
    # Reassign after sorting
    processes[:] = [p[0] for p in sorted_processes]
    bt[:] = [p[1] for p in sorted_processes]
    priority[:] = [p[2] for p in sorted_processes]

    # Waiting time for first process is 0
    wt[0] = 0

    # Calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def find_turn_around_time(n, bt, wt, tat):
    # Turnaround time = Burst time + Waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt, priority):
    wt = [0] * n
    tat = [0] * n

    # Find waiting time
    find_waiting_time(processes, n, bt, wt, priority)

    # Find turnaround time
    find_turn_around_time(n, bt, wt, tat)

    # Display processes with all details
    print("Processes   Burst Time   Priority   Waiting Time   Turnaround Time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"   {processes[i]} \t\t {bt[i]} \t\t {priority[i]} \t\t {wt[i]} \t\t {tat[i]}")

    print(f"\nAverage waiting time = {total_wt / n:.2f}")
    print(f"Average turnaround time = {total_tat / n:.2f}")

# Driver code
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3, 4]
    n = len(processes)

    # Burst time of all processes
    burst_time = [10, 1, 2, 1]

    # Priority of all processes (smaller number = higher priority)
    priority = [3, 1, 4, 2]

    find_avg_time(processes, n, burst_time, priority)
