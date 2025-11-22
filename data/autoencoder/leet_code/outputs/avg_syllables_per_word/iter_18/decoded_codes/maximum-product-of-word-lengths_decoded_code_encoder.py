from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        max_product = 0
        length = len(words)
        for i in range(length - 1):
            set_i = word_sets[i]
            len_i = len(words[i])
            for j in range(i + 1, length):
                set_j = word_sets[j]
                if set_i.isdisjoint(set_j):
                    product = len_i * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product