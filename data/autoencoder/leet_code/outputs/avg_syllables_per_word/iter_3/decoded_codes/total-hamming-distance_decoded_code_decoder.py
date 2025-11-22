class Solution:
    def totalHammingDistance(self, nums):
        total_distance = 0
        n = len(nums)
        for i in range(32):
            count_ones = sum((num >> i) & 1 for num in nums)
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        return total_distance