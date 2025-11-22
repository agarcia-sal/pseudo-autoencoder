from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]
        max_product = 0

        for i in range(len(words) - 1):
            set_i = word_sets[i]
            len_i = len(words[i])
            for j in range(i + 1, len(words)):
                # If no common characters between words[i] and words[j]
                if not set_i.intersection(word_sets[j]):
                    product = len_i * len(words[j])
                    if product > max_product:
                        max_product = product

        return max_product