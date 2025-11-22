from math import sqrt
from collections import Counter

def is_square(n):
    return int(sqrt(n)) ** 2 == n

def backtrack(path, count, nums_len):
    if len(path) == nums_len:
        return 1
    ans = 0
    for x in count:
        if count[x] > 0 and (not path or is_square(path[-1] + x)):
            count[x] -= 1
            ans += backtrack(path + [x], count, nums_len)
            count[x] += 1
    return ans

def num_squareful_perms(nums):
    count = Counter(nums)
    return backtrack([], count, len(nums))