class Solution:
    def totalHammingDistance(self, nums):
        total_distance = 0
        for i in range(32):
            count_ones = 0
            for num in nums:
                if ((num >> i) & 1) == 1:
                    count_ones += 1
            count_zeros = len(nums) - count_ones
            total_distance += count_ones * count_zeros
        return total_distance