from collections import Counter
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MODULO_VALUE = 10**9 + 7
        number_of_positions = len(words[0])
        target_length = len(target)

        # frequency_list[i]: Counter of characters at position i across all words
        frequency_list = [Counter() for _ in range(number_of_positions)]
        for word in words:
            for i, ch in enumerate(word):
                frequency_list[i][ch] += 1

        # dp_table[t][p]: number of ways to form first t chars of target using first p positions of words
        dp_table = [[0] * (number_of_positions + 1) for _ in range(target_length + 1)]

        # Base case: forming empty target (t=0) from any positions p is 1
        for p in range(number_of_positions + 1):
            dp_table[0][p] = 1

        for t in range(1, target_length + 1):
            current_char = target[t - 1]
            for p in range(1, number_of_positions + 1):
                # Ways without using the current position
                dp_table[t][p] = dp_table[t][p - 1]
                freq = frequency_list[p - 1].get(current_char, 0)
                if freq > 0:
                    # Ways using current character at position p-1
                    dp_table[t][p] = (dp_table[t][p] + dp_table[t - 1][p - 1] * freq) % MODULO_VALUE

        return dp_table[target_length][number_of_positions]