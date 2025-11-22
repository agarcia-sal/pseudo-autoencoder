from typing import List

class Solution:
    def findIntegers(self, n: int) -> int:
        # Get binary representation string of n without '0b' prefix
        bin_representation = bin(n)[2:]
        length = len(bin_representation)

        # dp[i] holds the count of valid binary strings of length i without consecutive ones
        dp: List[int] = [0] * (length + 1)
        dp[0] = 1  # Empty string count
        dp[1] = 2  # "0", "1"

        for i in range(2, length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        result = 0
        previous_bit = 0

        for i in range(length):
            if bin_representation[i] == '1':
                # Add counts of valid strings with length remaining that start with 0 at current bit
                result += dp[length - i - 1]
                if previous_bit == 1:
                    # Two consecutive ones encountered, subtract 1 and break
                    result -= 1
                    break
                previous_bit = 1
            else:
                previous_bit = 0

        return result + 1