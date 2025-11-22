def sortTransformedArray(nums, a, b, c):
    def quad(x):
        return a * x * x + b * x + c

    n = len(nums)
    res = [0] * n
    L, R = 0, n - 1

    if a >= 0:
        i = n - 1
        while L <= R:
            if quad(nums[L]) > quad(nums[R]):
                res[i] = quad(nums[L])
                L += 1
            else:
                res[i] = quad(nums[R])
                R -= 1
            i -= 1
    else:
        i = 0
        while L <= R:
            if quad(nums[L]) < quad(nums[R]):
                res[i] = quad(nums[L])
                L += 1
            else:
                res[i] = quad(nums[R])
                R -= 1
            i += 1
    return res