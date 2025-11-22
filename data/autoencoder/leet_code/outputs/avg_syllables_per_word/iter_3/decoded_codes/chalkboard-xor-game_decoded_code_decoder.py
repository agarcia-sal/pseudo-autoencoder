class Solution:
    def xorGame(self, nums):
        total_xor = 0
        for num in nums:
            total_xor ^= num
        if total_xor == 0 or len(nums) % 2 == 0:
            return True
        return False