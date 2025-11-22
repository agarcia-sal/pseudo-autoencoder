from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        max_product = 0

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if not word_sets[i].intersection(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product

        return max_product