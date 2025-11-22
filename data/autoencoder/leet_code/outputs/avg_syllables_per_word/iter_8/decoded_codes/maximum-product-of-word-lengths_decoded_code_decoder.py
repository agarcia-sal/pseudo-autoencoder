class Solution:
    def maxProduct(self, words):
        word_sets = []
        for word in words:
            word_sets.append(set(word))
        max_product = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product