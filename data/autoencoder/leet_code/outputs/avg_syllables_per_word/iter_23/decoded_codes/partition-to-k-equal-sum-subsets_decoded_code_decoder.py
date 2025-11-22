from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True)

        used = [False] * len(nums)

        def can_partition(index: int, k_remaining: int, current_sum: int) -> bool:
            if k_remaining == 0:
                return True
            if current_sum == target:
                # start to fill next subset
                return can_partition(0, k_remaining - 1, 0)

            for i in range(index, len(nums)):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if can_partition(i + 1, k_remaining, current_sum + nums[i]):
                        return True
                    used[i] = False
            return False

        return can_partition(0, k, 0)