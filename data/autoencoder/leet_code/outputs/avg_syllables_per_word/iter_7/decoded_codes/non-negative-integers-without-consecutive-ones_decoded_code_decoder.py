from typing import List

class Solution:
    def findIntegers(self, n: int) -> int:
        bin_rep: str = bin(n)[2:]
        length: int = len(bin_rep)

        dp: List[int] = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 2

        for i in range(2, length + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        result: int = 0
        prev_bit: int = 0

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