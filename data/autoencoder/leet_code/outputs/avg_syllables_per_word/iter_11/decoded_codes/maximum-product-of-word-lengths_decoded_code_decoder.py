class Solution:
    def maxProduct(self, words):
        word_sets = [set(word) for word in words]
        max_product = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product