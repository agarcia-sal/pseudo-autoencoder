from typing import List, Set

class Solution:
    def maxProduct(self, list_of_words: List[str]) -> int:
        list_of_character_sets = self.ConvertWordsToCharacterSets(list_of_words)
        maximum_product = 0
        n = len(list_of_words)
        for i in range(n):
            set_i = list_of_character_sets[i]
            len_i = len(list_of_words[i])
            for j in range(i + 1, n):
                if set_i.isdisjoint(list_of_character_sets[j]):
                    product = len_i * len(list_of_words[j])
                    if product > maximum_product:
                        maximum_product = product
        return maximum_product

    def ConvertWordsToCharacterSets(self, words: List[str]) -> List[Set[str]]:
        return [set(word) for word in words]