class Solution:
    def findIntegers(self, n: int) -> int:
        bin_rep = bin(n)[2:]
        length = len(bin_rep)

        dp = [0] * (length + 1)
        dp[0], dp[1] = 1, 2
        for i in range(2, length + 1):
            dp[i] = dp[i-1] + dp[i-2]

        result = 0
        prev_bit = 0
        for i in range(length):
            if bin_rep[i] == '1':
                result += dp[length - i - 1]
                if prev_bit == 1:
                    result -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0

        return result + 1