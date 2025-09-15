

#Code for cpu_fcfs

# FCFS Scheduling
def fcfs(processes, arrival, burst):
    n = len(processes)
    data = list(zip(processes, arrival, burst))
    # Sort by arrival time
    data.sort(key=lambda x: x[1])

    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n

    time = 0
    for i in range(n):
        pid, at, bt = data[i]
        if time < at:  # CPU idle
            time = at
        time += bt
        completion[i] = time
        turnaround[i] = completion[i] - at
        waiting[i] = turnaround[i] - bt

    avg_wt = sum(waiting) / n
    avg_tat = sum(turnaround) / n

    print("Process | AT | BT | CT | WT | TAT")
    for i in range(n):
        print(f"{data[i][0]:7} | {data[i][1]:2} | {data[i][2]:2} | {completion[i]:2} | {waiting[i]:2} | {turnaround[i]:3}")
    print(f"Average Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


# Example 1: With Arrival Time
processes = ["P1", "P2", "P3"]
arrival   = [0, 2, 4]
burst     = [5, 3, 8]
fcfs(processes, arrival, burst)

# Example 2: Without Arrival Time (just set AT=0 for all)
processes = ["P1", "P2", "P3"]
arrival   = [0, 0, 0]   # all 0 if not given
burst     = [5, 3, 8]
fcfs(processes, arrival, burst)


#Code for cpu_sjf

# SJF Scheduling
def sjf(processes, arrival, burst):
    n = len(processes)
    completed = [False] * n
    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n
    
    time = 0
    completed_count = 0
    
    while completed_count < n:
        # Select process with shortest burst among arrived ones
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if not completed[i] and arrival[i] <= time and burst[i] < min_bt:
                min_bt = burst[i]
                idx = i
        
        if idx == -1:  # No process has arrived yet
            time += 1
            continue
        
        time += burst[idx]
        completion[idx] = time
        turnaround[idx] = completion[idx] - arrival[idx]
        waiting[idx] = turnaround[idx] - burst[idx]
        completed[idx] = True
        completed_count += 1
    
    avg_wt = sum(waiting) / n
    avg_tat = sum(turnaround) / n
    
    print("Process | AT | BT | CT | WT | TAT")
    for i in range(n):
        print(f"{processes[i]:7} | {arrival[i]:2} | {burst[i]:2} | {completion[i]:2} | {waiting[i]:2} | {turnaround[i]:3}")
    print(f"Average Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


# Example
processes = ["P1", "P2", "P3", "P4"]
arrival   = [0, 1, 2, 3]
burst     = [7, 4, 1, 4]
sjf(processes, arrival, burst)



#Code for cpu_priority

# Priority Scheduling
def priority_scheduling(processes, arrival, burst, priority):
    n = len(processes)
    completed = [False] * n
    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n
    
    time = 0
    completed_count = 0
    
    while completed_count < n:
        # Select highest priority among arrived processes
        idx = -1
        max_priority = float('inf')
        for i in range(n):
            if not completed[i] and arrival[i] <= time and priority[i] < max_priority:
                max_priority = priority[i]
                idx = i
        
        if idx == -1:
            time += 1
            continue
        
        time += burst[idx]
        completion[idx] = time
        turnaround[idx] = completion[idx] - arrival[idx]
        waiting[idx] = turnaround[idx] - burst[idx]
        completed[idx] = True
        completed_count += 1
    
    avg_wt = sum(waiting) / n
    avg_tat = sum(turnaround) / n
    
    print("Process | AT | BT | PRI | CT | WT | TAT")
    for i in range(n):
        print(f"{processes[i]:7} | {arrival[i]:2} | {burst[i]:2} | {priority[i]:3} | {completion[i]:2} | {waiting[i]:2} | {turnaround[i]:3}")
    print(f"Average Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


# Example
processes = ["P1", "P2", "P3", "P4"]
arrival   = [0, 1, 2, 3]
burst     = [5, 3, 8, 6]
priority  = [2, 1, 4, 3]   # smaller = higher priority
priority_scheduling(processes, arrival, burst, priority)



#Code for cpu_rr

# Round Robin
def round_robin(processes, arrival, burst, quantum):
    n = len(processes)
    remaining = burst[:]  # copy burst times
    time = 0
    waiting = [0] * n
    turnaround = [0] * n
    completion = [0] * n
    
    ready_queue = []
    idx = 0
    
    while True:
        done = True
        for i in range(n):
            if remaining[i] > 0:
                done = False
                if remaining[i] > quantum:
                    time += quantum
                    remaining[i] -= quantum
                else:
                    time += remaining[i]
                    waiting[i] = time - burst[i] - arrival[i]
                    turnaround[i] = time - arrival[i]
                    completion[i] = time
                    remaining[i] = 0
        if done:
            break
    
    avg_wt = sum(waiting) / n
    avg_tat = sum(turnaround) / n
    
    print("Process | AT | BT | CT | WT | TAT")
    for i in range(n):
        print(f"{processes[i]:7} | {arrival[i]:2} | {burst[i]:2} | {completion[i]:2} | {waiting[i]:2} | {turnaround[i]:3}")
    print(f"Average Waiting Time = {avg_wt:.2f}")
    print(f"Average Turnaround Time = {avg_tat:.2f}")


# Example
processes = ["P1", "P2", "P3"]
arrival   = [0, 0, 0]   # all 0 for simplicity
burst     = [10, 5, 8]
round_robin(processes, arrival, burst, quantum=2)

#Code for page_fifo

# FIFO Page Replacement
List = [1,2,2,3,4,5,2,6,3]
page_size = 3
frames = []
faults = 0

print(f"{'Step':<5}{'Page':<6}{'Frames':<15}{'Fault?'}")
print("-"*35)

for step, page in enumerate(List, start=1):
    if page in frames:
        # Page hit → nothing changes
        fault = "No"
    else:
        # Page fault
        faults += 1
        fault = "Yes"
        if len(frames) < page_size:
            frames.append(page)
        else:
            frames.pop(0)     # FIFO → remove oldest
            frames.append(page)
    
    print(f"{step:<5}{page:<6}{str(frames):<15}{fault}")

print("-"*35)
print("Total Page Faults:", faults)
print("Fault Rate: {:.2f}%".format(faults/len(List)*100))


#Code for page_opt

# OPT (Optimal) Page Replacement
def optimal(pages, page_size):
    frames = []
    faults = 0
    
    print(f"{'Step':<5}{'Page':<6}{'Frames':<15}{'Fault?'}")
    print("-"*35)
    
    for i, page in enumerate(pages, start=1):
        if page in frames:
            fault = "No"
        else:
            faults += 1
            fault = "Yes"
            if len(frames) < page_size:
                frames.append(page)
            else:
                # find page to replace
                future = pages[i:]
                index = -1
                farthest = -1
                for f in frames:
                    if f in future:
                        pos = future.index(f)
                        if pos > farthest:
                            farthest = pos
                            index = frames.index(f)
                    else:
                        index = frames.index(f)
                        break
                frames[index] = page
        print(f"{i:<5}{page:<6}{str(frames):<15}{fault}")
    
    print("-"*35)
    print("Total Page Faults:", faults)
    print("Fault Rate: {:.2f}%".format(faults/len(pages)*100))


# Example
pages = [1,2,2,3,4,5,2,6,3]
optimal(pages, 3)



#Code for page_lru

# LRU Page Replacement
def lru(pages, page_size):
    frames = []
    faults = 0
    recent = {}  # track last used index
    
    print(f"{'Step':<5}{'Page':<6}{'Frames':<15}{'Fault?'}")
    print("-"*35)
    
    for i, page in enumerate(pages, start=1):
        if page in frames:
            fault = "No"
        else:
            faults += 1
            fault = "Yes"
            if len(frames) < page_size:
                frames.append(page)
            else:
                # find least recently used page
                lru_page = min(frames, key=lambda x: recent.get(x, -1))
                frames[frames.index(lru_page)] = page
        recent[page] = i   # update last used
        print(f"{i:<5}{page:<6}{str(frames):<15}{fault}")
    
    print("-"*35)
    print("Total Page Faults:", faults)
    print("Fault Rate: {:.2f}%".format(faults/len(pages)*100))


# Example
pages = [1,2,2,3,4,5,2,6,3]
lru(pages, 3)



#Code for mem_firstfit

# First Fit Memory Allocation
def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, psize in enumerate(processes):
        for j, bsize in enumerate(blocks):
            if bsize >= psize:
                allocation[i] = j
                blocks[j] -= psize
                break
    return allocation

def print_allocation(processes, allocation):
    print("Process No.	Process Size	Block No.")
    for i, (psize, block) in enumerate(zip(processes, allocation)):
        if block != -1:
            print(f"P{i+1}		{psize}		{block+1}")
        else:
            print(f"P{i+1}		{psize}		Not Allocated")


blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("Initial Blocks:", blocks)
print("Processes:", processes)

allocation = first_fit (blocks, processes)
print("--- First Fit Allocation ---")
print_allocation(processes, allocation)


#Code for mem_bestfit

# Best Fit Memory Allocation
def best_fit (blocks, processes):
    allocation = [-1] * len(processes)
    for i, psize in enumerate(processes):
        best_idx = -1
        for j, bsize in enumerate(blocks):
            if bsize >= psize:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= psize
    return allocation

def print_allocation (processes, allocation):
    print("Process No.	Process Size	Block No.")
    for i, (psize, block) in enumerate(zip(processes, allocation)):
        if block != -1:
            print(f"P{i+1}		{psize}		{block+1}")
        else:
            print(f"P{i+1}		{psize}		Not Allocated")


blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("Initial Blocks:", blocks)
print("Processes:", processes)

allocation = best_fit (blocks, processes)
print("--- Best Fit Allocation ---")
print_allocation(processes, allocation)


#Code for mem_worstfit

# Worst Fit Memory Allocation
def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, psize in enumerate(processes):
        worst_idx = -1
        for j, bsize in enumerate(blocks):
            if bsize >= psize:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= psize
    return allocation

def print_allocation (processes, allocation):
    print("Process No.	Process Size	Block No.")
    for i, (psize, block) in enumerate(zip(processes, allocation)):
        if block != -1:
            print(f"P{i+1}		{psize}		{block+1}")
        else:
            print(f"P{i+1}		{psize}		Not Allocated")


blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("Initial Blocks:", blocks)
print("Processes:", processes)

allocation = worst_fit (blocks, processes)
print("--- Worst Fit Allocation ---")
print_allocation(processes, allocation)
