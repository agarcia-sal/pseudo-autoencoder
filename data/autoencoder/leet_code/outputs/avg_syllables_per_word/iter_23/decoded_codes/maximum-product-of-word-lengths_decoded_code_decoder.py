from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        max_product = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if word_sets[i].isdisjoint(word_sets[j]):  # no common characters
                    product = len(words[i]) * len(words[j])
                    if max_product < product:
                        max_product = product
        return max_product