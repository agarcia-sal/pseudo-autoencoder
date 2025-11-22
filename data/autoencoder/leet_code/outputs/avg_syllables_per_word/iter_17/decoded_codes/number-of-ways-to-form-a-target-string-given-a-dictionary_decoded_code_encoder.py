from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        word_length = len(words[0])
        target_length = len(target)

        frequency_list = self.initialize_frequency_list(word_length)
        for word in words:
            for pos in range(word_length):
                char = word[pos]
                frequency_list[pos][char] += 1

        dp_table = self.initialize_dp_table(target_length + 1, word_length + 1)
        for col in range(word_length + 1):
            dp_table[0][col] = 1

        for i in range(1, target_length + 1):
            target_char = target[i - 1]
            for j in range(1, word_length + 1):
                dp_table[i][j] = dp_table[i][j - 1]
                freq = frequency_list[j - 1].get(target_char, 0)
                if freq > 0:
                    dp_table[i][j] += dp_table[i - 1][j - 1] * freq
                    dp_table[i][j] %= MOD

        return dp_table[target_length][word_length]

    def initialize_frequency_list(self, length_of_words: int):
        return [defaultdict(int) for _ in range(length_of_words)]

    def initialize_dp_table(self, rows: int, columns: int):
        return [[0] * columns for _ in range(rows)]