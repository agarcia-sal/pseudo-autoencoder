from collections import deque

def min_mutation(start, end, bank):
    s = set(bank)
    q = deque([(start, 0)])
    mp = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}

    while q:
        t, step = q.popleft()
        if t == end:
            return step
        for i, v in enumerate(t):
            for j in mp[v]:
                nxt = t[:i] + j + t[i+1:]
                if nxt in s:
                    q.append((nxt, step + 1))
                    s.remove(nxt)
    return -1