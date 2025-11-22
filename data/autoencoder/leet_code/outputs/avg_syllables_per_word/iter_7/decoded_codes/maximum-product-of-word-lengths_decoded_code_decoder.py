from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        max_product = 0
        length = len(words)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product