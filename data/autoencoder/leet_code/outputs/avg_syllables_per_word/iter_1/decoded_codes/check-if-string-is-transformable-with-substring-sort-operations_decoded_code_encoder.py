import heapq

def check_order(s, t):
    pos = {i: [] for i in range(10)}
    for i, c in enumerate(s):
        heapq.heappush(pos[int(c)], i)

    for c in t:
        d = int(c)
        if not pos[d]:
            return False
        for x in range(d):
            if pos[x] and pos[x][0] < pos[d][0]:
                return False
        heapq.heappop(pos[d])

    return True