def optimal(pages, capacity):
    s = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.append(pages[i])
            else:
                # find page not used for longest time
                farthest = -1
                index = -1
                for j in range(len(s)):
                    try:
                        next_use = pages[i+1:].index(s[j])
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index = j
                s[index] = pages[i]
            page_faults += 1
    return page_faults

# Example
print("OPT Page Faults:", optimal(pages, capacity))
