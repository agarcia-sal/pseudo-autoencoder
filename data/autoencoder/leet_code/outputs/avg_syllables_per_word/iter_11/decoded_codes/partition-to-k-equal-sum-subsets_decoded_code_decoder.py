class Solution:
    def canPartitionKSubsets(self, nums, k):
        total_sum = 0
        for number in nums:
            total_sum += number
        if total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True)

        def can_partition(index, k, current_sum, used):
            if k == 0:
                return True
            if current_sum == target:
                return can_partition(0, k - 1, 0, used)
            for i in range(index, len(nums)):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if can_partition(i + 1, k, current_sum + nums[i], used):
                        return True
                    used[i] = False
            return False

        used = [False] * len(nums)
        return can_partition(0, k, 0, used)