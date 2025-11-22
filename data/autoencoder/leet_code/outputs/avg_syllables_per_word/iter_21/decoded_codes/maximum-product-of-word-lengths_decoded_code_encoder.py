class Solution:
    def maxProduct(self, words):
        word_sets = self.convert_words_to_character_sets(words)
        max_product = 0
        n = len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product

    def convert_words_to_character_sets(self, words):
        return [set(word) for word in words]