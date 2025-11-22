from typing import List, Set

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets: List[Set[str]] = [set(word) for word in words]

        max_product = 0
        n = len(words)
        for i in range(n - 1):
            set_i = word_sets[i]
            len_i = len(words[i])
            for j in range(i + 1, n):
                # If no common characters between words[i] and words[j]
                if set_i.isdisjoint(word_sets[j]):
                    product = len_i * len(words[j])
                    if product > max_product:
                        max_product = product

        return max_product