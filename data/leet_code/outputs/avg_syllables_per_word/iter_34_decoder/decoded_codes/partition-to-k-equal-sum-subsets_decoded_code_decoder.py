from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        nums.sort(reverse=True)

        used = [False] * len(nums)

        def can_partition(index: int, k_remaining: int, current_sum: int, used_flags: List[bool]) -> bool:
            if k_remaining == 0:
                return True
            if current_sum == target:
                return can_partition(0, k_remaining - 1, 0, used_flags)

            for pos in range(index, len(nums)):
                if not used_flags[pos] and current_sum + nums[pos] <= target:
                    used_flags[pos] = True
                    if can_partition(pos + 1, k_remaining, current_sum + nums[pos], used_flags):
                        return True
                    used_flags[pos] = False
            return False

        return can_partition(0, k, 0, used)