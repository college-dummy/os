# Memory Management Algorithms: First Fit, Best Fit, Worst Fit

def first_fit(block_size, m, process_size, n):
    allocation = [-1] * n  # stores block index for each process

    for i in range(n):  # pick each process
        for j in range(m):  # check each block
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break

    print("\nFirst Fit Allocation:")
    print_allocation(process_size, allocation)


def best_fit(block_size, m, process_size, n):
    allocation = [-1] * n

    for i in range(n):
        best_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if best_idx == -1 or block_size[j] < block_size[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            block_size[best_idx] -= process_size[i]

    print("\nBest Fit Allocation:")
    print_allocation(process_size, allocation)


def worst_fit(block_size, m, process_size, n):
    allocation = [-1] * n

    for i in range(n):
        worst_idx = -1
        for j in range(m):
            if block_size[j] >= process_size[i]:
                if worst_idx == -1 or block_size[j] > block_size[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            block_size[worst_idx] -= process_size[i]

    print("\nWorst Fit Allocation:")
    print_allocation(process_size, allocation)


def print_allocation(process_size, allocation):
    print("Process No.   Process Size   Block No.")
    for i in range(len(process_size)):
        if allocation[i] != -1:
            print(f"   {i+1}\t\t{process_size[i]}\t\t{allocation[i]+1}")
        else:
            print(f"   {i+1}\t\t{process_size[i]}\t\tNot Allocated")


# Driver Code
if __name__ == "__main__":
    block_size = [100, 500, 200, 300, 600]   # memory blocks
    process_size = [212, 417, 112, 426]      # process sizes

    m = len(block_size)  # number of blocks
    n = len(process_size)  # number of processes

    # Run all algorithms
    first_fit(block_size[:], m, process_size, n)
    best_fit(block_size[:], m, process_size, n)
    worst_fit(block_size[:], m, process_size, n)
