# CPU Scheduling - Round Robin

def find_waiting_time(processes, n, bt, wt, quantum):
    rem_bt = bt[:]  # copy of burst times
    t = 0  # current time

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    # process gets full quantum
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    # process finishes execution
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

def find_turn_around_time(n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, bt, wt, quantum)
    find_turn_around_time(n, bt, wt, tat)

    print(f"Time Quantum = {quantum}")
    print("Processes   Burst Time   Waiting Time   Turnaround Time")

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
    processes = [1, 2, 3]
    n = len(processes)

    burst_time = [10, 5, 8]
    quantum = 2  # time slice

    find_avg_time(processes, n, burst_time, quantum)
