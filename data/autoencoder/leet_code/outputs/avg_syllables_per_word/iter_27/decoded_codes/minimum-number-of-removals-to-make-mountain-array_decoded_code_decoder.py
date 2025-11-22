from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0  # Cannot form a mountain array if less than 3 elements

        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        max_mountain_length = 0
        # Peak can't be first or last element, so i in [1, n-2]
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)

        return n - max_mountain_length