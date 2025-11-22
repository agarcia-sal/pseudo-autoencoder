class Solution:
    def countSpecialSubsequences(self, nums):
        MODULO_VALUE = 10**9 + 7
        dp_zero = 0
        dp_one = 0
        dp_two = 0

        for number in nums:
            if number == 0:
                dp_zero = (dp_zero * 2 + 1) % MODULO_VALUE
            elif number == 1:
                dp_one = (dp_one * 2 + dp_zero) % MODULO_VALUE
            elif number == 2:
                dp_two = (dp_two * 2 + dp_one) % MODULO_VALUE

        return dp_two