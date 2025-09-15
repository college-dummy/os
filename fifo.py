# CPU Scheduling - First Come First Serve (FIFO / FCFS)

def find_waiting_time(processes, n, bt, wt):
    # waiting time for first process is 0
    wt[0] = 0

    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def find_turn_around_time(processes, n, bt, wt, tat):
    # turnaround time = burst time + waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # function to find waiting time of all processes
    find_waiting_time(processes, n, bt, wt)

    # function to find turn around time for all processes
    find_turn_around_time(processes, n, bt, wt, tat)

    # display processes with all details
    print("Processes   Burst time   Waiting time   Turnaround time")

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"   {processes[i]} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")

    print(f"\nAverage waiting time = {total_wt / n:.2f}")
    print(f"Average turnaround time = {total_tat / n:.2f}")

# Driver code
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3]
    n = len(processes)

    # Burst time of all processes
    burst_time = [10, 5, 8]

    find_avg_time(processes, n, burst_time)
