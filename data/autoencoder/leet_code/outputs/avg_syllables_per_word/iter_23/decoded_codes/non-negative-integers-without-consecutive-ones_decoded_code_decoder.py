class Solution:
    def findIntegers(self, n: int) -> int:
        bin_representation = bin(n)[2:]  # binary form of n without '0b'
        the_length = len(bin_representation)
        dp = [0] * (the_length + 1)
        dp[0] = 1
        if the_length >= 1:
            dp[1] = 2
        for i in range(2, the_length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        result = 0
        prev_bit = 0
        for i in range(the_length):
            if bin_representation[i] == '1':
                result += dp[the_length - i - 1]
                if prev_bit == 1:
                    result -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1