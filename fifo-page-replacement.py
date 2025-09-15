def fifo(pages, capacity):
    s = []
    page_faults = 0

    for page in pages:
        if page not in s:
            if len(s) < capacity:
                s.append(page)
            else:
                s.pop(0)  # remove oldest
                s.append(page)
            page_faults += 1
    return page_faults

# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
print("FIFO Page Faults:", fifo(pages, capacity))
