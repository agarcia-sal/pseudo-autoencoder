def leastOpsExpressTarget(x, target):
    from math import log

    def dp(t):
        if t == 0:
            return -1
        if t < x:
            return min(2 * t - 1, 2 * (x - t))
        p = int(log(t, x))
        xp = x ** p
        res = dp(t - xp) + p
        if x ** (p + 1) - t < t:
            res = min(res, dp(x ** (p + 1) - t) + p + 1)
        return res

    return dp(target)