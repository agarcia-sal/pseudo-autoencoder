from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n == 0:
            return []

        f = [1] * n
        k = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[i] < f[j] + 1:
                        f[i] = f[j] + 1
            if f[k] < f[i]:
                k = i

        m = f[k]
        i = k
        ans = []
        while m > 0 and i >= 0:
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k = i
                m -= 1
            i -= 1

        return ans[::-1]