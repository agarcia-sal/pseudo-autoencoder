from math import comb

MOD = 10**9 + 7

def count_ways(arr):
    if len(arr) <= 1:
        return 1
    root = arr[0]
    L = [x for x in arr if x < root]
    R = [x for x in arr if x > root]
    left_ways = count_ways(L)
    right_ways = count_ways(R)
    interleave = comb(len(L) + len(R), len(L))
    return (left_ways * right_ways * interleave) % MOD

# Example usage:
# nums = [...]
# print((count_ways(nums) - 1) % MOD)