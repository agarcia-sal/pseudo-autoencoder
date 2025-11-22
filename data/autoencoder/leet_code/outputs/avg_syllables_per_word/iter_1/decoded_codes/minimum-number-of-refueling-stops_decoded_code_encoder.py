import heapq

def minRefuelStops(target, startFuel, stations):
    max_heap = []
    fuel = startFuel
    stops = 0
    stations.append([target, 0])

    for pos, f in stations:
        while max_heap and fuel < pos:
            fuel += -heapq.heappop(max_heap)
            stops += 1
        if fuel < pos:
            return -1
        heapq.heappush(max_heap, -f)
    return stops