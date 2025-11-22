import heapq

def find_max_capital(k, w, profits, capital):
    projects = sorted(zip(capital, profits), key=lambda x: x[0])
    max_heap = []
    i = 0
    n = len(projects)

    for _ in range(k):
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1
        if not max_heap:
            break
        w += -heapq.heappop(max_heap)
    return w