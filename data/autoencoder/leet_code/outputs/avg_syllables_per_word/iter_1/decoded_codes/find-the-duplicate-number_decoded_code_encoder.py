from bisect import bisect_left

def func(nums):
    def f(x):
        count = sum(v <= x for v in nums)
        return count > x
    return bisect_left(range(len(nums)), True, key=f)