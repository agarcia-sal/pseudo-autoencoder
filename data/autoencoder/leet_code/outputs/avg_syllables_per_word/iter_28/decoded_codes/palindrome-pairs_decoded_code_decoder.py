from typing import List, Dict

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        word_dict: Dict[str, int] = {}
        for index, word in enumerate(words):
            word_dict[word] = index

        result: List[List[int]] = []

        for index, word in enumerate(words):
            if word == "":
                continue

            # Check pairs with empty string word
            if "" in word_dict and is_palindrome(word):
                empty_index = word_dict[""]
                result.append([index, empty_index])
                result.append([empty_index, index])

            reversed_word = word[::-1]
            if reversed_word in word_dict and word_dict[reversed_word] != index:
                result.append([index, word_dict[reversed_word]])

            for j in range(1, len(word)):
                prefix = word[:j]
                suffix = word[j:]
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]

                if is_palindrome(suffix) and reversed_prefix in word_dict:
                    result.append([index, word_dict[reversed_prefix]])

                if is_palindrome(prefix) and reversed_suffix in word_dict:
                    result.append([word_dict[reversed_suffix], index])

        return result