from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k

        nums.sort(reverse=True)
        n = len(nums)

        # Early pruning: if the largest number is greater than target,
        # partition not possible
        if nums[0] > target:
            return False

        used = [False] * n

        def can_partition(index: int, k_left: int, current_sum: int) -> bool:
            if k_left == 0:
                return True
            if current_sum == target:
                # Start next subset from beginning of array
                return can_partition(0, k_left - 1, 0)

            prev = -1  # to avoid duplicate processing in the same recursive level
            for i in range(index, n):
                if not used[i] and current_sum + nums[i] <= target:
                    # Skip duplicates
                    if nums[i] == prev:
                        continue
                    used[i] = True
                    if can_partition(i + 1, k_left, current_sum + nums[i]):
                        return True
                    used[i] = False
                    prev = nums[i]
            return False

        return can_partition(0, k, 0)