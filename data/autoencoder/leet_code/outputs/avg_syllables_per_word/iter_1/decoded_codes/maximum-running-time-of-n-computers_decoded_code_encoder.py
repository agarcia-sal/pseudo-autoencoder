def maxRunTime(n, batteries):
    def canRunFor(t):
        return sum(min(b, t) for b in batteries) >= t * n

    left, right = 0, sum(batteries) // n
    while left < right:
        mid = (left + right + 1) // 2
        if canRunFor(mid):
            left = mid
        else:
            right = mid - 1
    return left