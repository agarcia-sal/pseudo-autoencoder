from collections import Counter
from typing import List

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        first = nums[0]

        for i in range(1, n):
            diff = nums[i] - first
            if diff <= 0 or diff % 2 != 0:
                continue
            k = diff // 2

            count = Counter(nums)
            arr = []
            for x in nums:
                if count[x] == 0:
                    continue
                if count[x + 2 * k] == 0:
                    break
                arr.append(x + k)
                count[x] -= 1
                count[x + 2 * k] -= 1
            if len(arr) == n // 2:
                return arr

        return []