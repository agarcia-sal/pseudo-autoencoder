def min_operations(nums):
    n = len(nums)
    u = sorted(set(nums))
    res = n
    j = 0
    for i in range(len(u)):
        while j < len(u) and u[j] < u[i] + n:
            j += 1
        res = min(res, n - (j - i))
    return res