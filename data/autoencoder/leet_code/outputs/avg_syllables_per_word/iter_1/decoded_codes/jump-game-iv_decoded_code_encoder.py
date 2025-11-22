from collections import defaultdict, deque

def min_jumps(arr):
    n = len(arr)
    if n == 1:
        return 0

    map = defaultdict(list)
    for i, v in enumerate(arr):
        map[v].append(i)

    q = deque([(0, 0)])
    vis = {0}

    while q:
        i, s = q.popleft()
        if i == n - 1:
            return s

        nxt = [i - 1, i + 1] + map[arr[i]]
        for x in nxt:
            if 0 <= x < n and x not in vis:
                vis.add(x)
                q.append((x, s + 1))

        map[arr[i]] = []

    return -1