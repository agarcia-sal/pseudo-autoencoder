def isSelfCrossing(dist):
    n = len(dist)
    if n < 4:
        return False

    for i in range(3, n):
        if dist[i] >= dist[i-2] and dist[i-1] <= dist[i-3]:
            return True
        if i >= 4 and dist[i-1] == dist[i-3] and dist[i] + dist[i-4] >= dist[i-2]:
            return True
        if (i >= 5 and dist[i-2] >= dist[i-4] and dist[i-3] >= dist[i-1] 
            and dist[i-1] + dist[i-5] >= dist[i-3] and dist[i] + dist[i-4] >= dist[i-2]):
            return True

    return False