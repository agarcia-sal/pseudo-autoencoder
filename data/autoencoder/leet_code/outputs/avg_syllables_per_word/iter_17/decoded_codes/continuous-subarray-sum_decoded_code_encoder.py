class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_index_map = {0: -1}
        cumulative_sum = 0
        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:
                cumulative_sum %= k
            if cumulative_sum in remainder_index_map:
                if i - remainder_index_map[cumulative_sum] > 1:
                    return True
            else:
                remainder_index_map[cumulative_sum] = i
        return False