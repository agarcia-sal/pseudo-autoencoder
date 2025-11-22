def maxDistToClosest(seats):
    n = len(seats)
    start = next(i for i, seat in enumerate(seats) if seat == 1)
    end = n - 1 - next(i for i, seat in enumerate(reversed(seats)) if seat == 1)
    max_dist = max(start, n - end - 1)
    cur_dist = 0
    for i in range(start, end + 1):
        if seats[i] == 0:
            cur_dist += 1
            max_dist = max(max_dist, (cur_dist + 1) // 2)
        else:
            cur_dist = 0
    return max_dist