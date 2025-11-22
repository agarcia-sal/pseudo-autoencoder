from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MODULO_DIVISOR = 10**9 + 7
        length_of_word = len(words[0])
        length_of_target = len(target)

        # frequency maps for each position in the words
        freq_maps = [defaultdict(int) for _ in range(length_of_word)]

        for word in words:
            for idx, ch in enumerate(word):
                freq_maps[idx][ch] += 1

        # dp_table dimensions: (length_of_target + 1) x (length_of_word + 1)
        dp_table = [[0] * (length_of_word + 1) for _ in range(length_of_target + 1)]

        # base case: empty target can be formed in one way from any prefix of words
        for i in range(length_of_word + 1):
            dp_table[0][i] = 1

        for target_pos in range(1, length_of_target + 1):
            current_target_char = target[target_pos - 1]
            for word_pos in range(1, length_of_word + 1):
                dp_table[target_pos][word_pos] = dp_table[target_pos][word_pos - 1]
                current_frequency = freq_maps[word_pos - 1].get(current_target_char, 0)
                if current_frequency > 0:
                    dp_table[target_pos][word_pos] += dp_table[target_pos - 1][word_pos - 1] * current_frequency
                    dp_table[target_pos][word_pos] %= MODULO_DIVISOR

        return dp_table[length_of_target][length_of_word]