from typing import List, Dict

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        word_dict: Dict[str, int] = {word: i for i, word in enumerate(words)}
        result: List[List[int]] = []

        for i, word in enumerate(words):
            if word == "":
                continue

            if "" in word_dict and is_palindrome(word):
                empty_pos = word_dict[""]
                result.append([i, empty_pos])
                result.append([empty_pos, i])

            reversed_word = word[::-1]
            if reversed_word in word_dict and word_dict[reversed_word] != i:
                result.append([i, word_dict[reversed_word]])

            length = len(word)
            for j in range(1, length):
                prefix = word[:j]
                suffix = word[j:]
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]

                if is_palindrome(suffix) and reversed_prefix in word_dict:
                    result.append([i, word_dict[reversed_prefix]])
                if is_palindrome(prefix) and reversed_suffix in word_dict:
                    result.append([word_dict[reversed_suffix], i])

        return result