class Solution:
    def countSpecialSubsequences(self, nums):
        MODULO = 10**9 + 7
        dp_at_zero = 0
        dp_at_one = 0
        dp_at_two = 0

        for num in nums:
            if num == 0:
                dp_at_zero = (2 * dp_at_zero + 1) % MODULO
            elif num == 1:
                dp_at_one = (2 * dp_at_one + dp_at_zero) % MODULO
            elif num == 2:
                dp_at_two = (2 * dp_at_two + dp_at_one) % MODULO

        return dp_at_two