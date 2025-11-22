class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for number in nums:
            ones = (ones ^ number) & ~twos
            twos = (twos ^ number) & ~ones
        return ones