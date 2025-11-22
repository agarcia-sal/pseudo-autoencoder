from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        f = [1] * n
        k = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
            if f[k] < f[i]:
                k = i
        m = f[k]
        ans = []
        i = n - 1
        while m > 0 and i >= 0:
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k = i
                m -= 1
            i -= 1
        return ans[::-1]