from typing import Dict

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MODULO = 10**9 + 7
        length_of_s = len(s)
        dp = [0] * (length_of_s + 1)
        dp[0] = 1
        last_occurrence: Dict[str, int] = {}

        for index in range(1, length_of_s + 1):
            current_character = s[index - 1]
            dp[index] = (dp[index - 1] * 2) % MODULO
            if current_character in last_occurrence:
                dp[index] = (dp[index] - dp[last_occurrence[current_character] - 1] + MODULO) % MODULO
            last_occurrence[current_character] = index

        return (dp[length_of_s] - 1) % MODULO