def lru(pages, capacity):
    s = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in s:
            if len(s) < capacity:
                s.append(pages[i])
            else:
                # remove least recently used
                lru_index = min(range(len(s)), key=lambda x: 
                                (pages[:i][::-1].index(s[x]) 
                                 if s[x] in pages[:i] else float('inf')))
                s[lru_index] = pages[i]
            page_faults += 1
    return page_faults

# Example
print("LRU Page Faults:", lru(pages, capacity))
