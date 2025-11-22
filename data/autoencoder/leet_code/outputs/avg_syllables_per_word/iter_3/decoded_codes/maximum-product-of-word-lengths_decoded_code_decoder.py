class Solution:
    def maxProduct(self, words):
        word_sets = [set(word) for word in words]
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not word_sets[i] & word_sets[j]:
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product