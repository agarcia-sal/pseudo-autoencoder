from bisect import bisect_left

def max_assignable_tasks(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()

    def canAssign(k):
        W = workers[-k:]
        used = 0
        for i in range(k - 1, -1, -1):
            t = tasks[i]
            idx = bisect_left(W, t)
            if idx < len(W):
                W.pop(idx)
            elif used < pills:
                idx = bisect_left(W, t - strength)
                if idx < len(W):
                    W.pop(idx)
                    used += 1
                else:
                    return False
            else:
                return False
        return True

    left, right = 0, min(len(tasks), len(workers)) + 1
    while left < right:
        mid = (left + right) // 2
        if canAssign(mid):
            left = mid + 1
        else:
            right = mid
    return left - 1