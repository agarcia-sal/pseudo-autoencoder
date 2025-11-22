class Solution:
    def maxProduct(self, words):
        word_sets = self.create_character_sets(words)
        max_product = 0
        n = len(words)
        for i in range(n - 1):
            set_i = word_sets[i]
            len_i = len(words[i])
            for j in range(i + 1, n):
                if not set_i & word_sets[j]:  # no common characters
                    product = len_i * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product

    def create_character_sets(self, words):
        character_sets = []
        for word in words:
            character_sets.append(set(word))
        return character_sets