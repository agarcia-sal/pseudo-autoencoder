from collections import defaultdict
from itertools import combinations

def min_subset_sum_difference(nums):
    n = len(nums) // 2
    total = sum(nums)
    target = total / 2
    minDiff = float('inf')

    L, R = nums[:n], nums[n:]
    leftSums = [defaultdict(int) for _ in range(n+1)]
    rightSums = [defaultdict(int) for _ in range(n+1)]

    for i in range(n+1):
        for combo in combinations(L, i):
            leftSums[i][sum(combo)] += 1
        for combo in combinations(R, i):
            rightSums[i][sum(combo)] += 1

    for i in range(n+1):
        leftVals = sorted(leftSums[i].keys())
        rightVals = sorted(rightSums[n - i].keys())

        j, k = 0, len(rightVals) - 1
        while j < len(leftVals) and k >= 0:
            curr = leftVals[j] + rightVals[k]
            diff = abs(total - 2*curr)
            minDiff = min(minDiff, diff)
            if curr < target:
                j += 1
            elif curr > target:
                k -= 1
            else:
                return 0

    return minDiff