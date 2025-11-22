from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n == 0:
            return []

        f = [1] * n  # f[i] stores the length of the largest divisible subset ending with nums[i]
        k = 0  # index of the largest subset's last element

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[i] < f[j] + 1:
                        f[i] = f[j] + 1
            if f[k] < f[i]:
                k = i

        m = f[k]  # length of largest divisible subset
        i = k
        ans = []
        while m > 0 and i >= 0:
            # Check conditions to include nums[i] in the answer subset:
            # nums[k] % nums[i] == 0 ensures divisibility along the subset,
            # f[i] == m ensures length consistency.
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k = i
                m -= 1
            i -= 1

        return ans[::-1]  # reverse to get ascending order subset