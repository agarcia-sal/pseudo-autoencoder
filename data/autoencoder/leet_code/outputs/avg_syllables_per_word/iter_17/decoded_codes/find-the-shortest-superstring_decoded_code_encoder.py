from math import inf
from functools import lru_cache

class Solution:
    def shortestSuperstring(self, list_of_words):
        number_of_words = len(list_of_words)

        def overlap(index_i, index_j):
            w1, w2 = list_of_words[index_i], list_of_words[index_j]
            max_len = min(len(w1), len(w2))
            for k in range(max_len, 0, -1):
                if w1[-k:] == w2[:k]:
                    return k
            return 0

        @lru_cache(None)
        def dp(mask, index_i):
            if mask == (1 << number_of_words) - 1:
                return 0, ''

            minimum_length = inf
            best_path = ''
            for index_j in range(number_of_words):
                if not (mask & (1 << index_j)):
                    length, path = dp(mask | (1 << index_j), index_j)
                    overlap_len = overlap(index_i, index_j)
                    length += len(list_of_words[index_j]) - overlap_len
                    if length < minimum_length:
                        minimum_length = length
                        best_path = list_of_words[index_j][overlap_len:] + path
            return minimum_length, best_path

        minimum_length = inf
        shortest_path = ''
        for index_i in range(number_of_words):
            length, path = dp(1 << index_i, index_i)
            length += len(list_of_words[index_i])
            if length < minimum_length:
                minimum_length = length
                shortest_path = list_of_words[index_i] + path

        return shortest_path