class Solution:
    def findIntegers(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        length_of_representation = len(binary_representation)

        dp = [0] * (length_of_representation + 1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, length_of_representation + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        result = 0
        previous_bit = 0

        for i in range(length_of_representation):
            if binary_representation[i] == '1':
                result += dp[length_of_representation - i - 1]
                if previous_bit == 1:
                    result -= 1
                    break
                previous_bit = 1
            else:
                previous_bit = 0

        return result + 1