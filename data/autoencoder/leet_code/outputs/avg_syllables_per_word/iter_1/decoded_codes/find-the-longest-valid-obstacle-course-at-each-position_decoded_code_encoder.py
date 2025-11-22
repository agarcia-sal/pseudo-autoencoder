from bisect import bisect_right

def process_obstacles(obstacles):
    incr = []
    ans = []
    for ob in obstacles:
        i = bisect_right(incr, ob)
        if i == len(incr):
            incr.append(ob)
        else:
            incr[i] = ob
        ans.append(i+1)
    return ans