class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        word_dict = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            if word == "":
                continue

            if "" in word_dict and is_palindrome(word):
                result.append([i, word_dict[""]])
                result.append([word_dict[""], i])

            reversed_word = word[::-1]
            if reversed_word in word_dict and word_dict[reversed_word] != i:
                result.append([i, word_dict[reversed_word]])

            for j in range(1, len(word)):
                prefix, suffix = word[:j], word[j:]
                reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]

                if is_palindrome(suffix) and reversed_prefix in word_dict:
                    result.append([i, word_dict[reversed_prefix]])
                if is_palindrome(prefix) and reversed_suffix in word_dict:
                    result.append([word_dict[reversed_suffix], i])

        return result