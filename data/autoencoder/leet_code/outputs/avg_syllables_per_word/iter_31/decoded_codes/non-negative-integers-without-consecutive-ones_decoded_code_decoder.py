class Solution:
    def findIntegers(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        length = len(binary_representation)

        if length == 0:
            return 1  # only 0

        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        result = 0
        previous_bit = 0
        for i in range(length):
            if binary_representation[i] == '1':
                result += dp[length - i - 1]
                if previous_bit == 1:
                    result -= 1
                    break
                previous_bit = 1
            else:
                previous_bit = 0

        return result + 1