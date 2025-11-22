from math import factorial

def getPermutation(n, k):
    nums = list(range(1, n + 1))
    k -= 1
    res = []
    for i in range(n, 0, -1):
        f = factorial(i - 1)
        idx = k // f
        res.append(str(nums[idx]))
        nums.pop(idx)
        k %= f
    return ''.join(res)