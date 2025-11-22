class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        word_dictionary = self.create_word_dictionary(words)
        result = []

        for i in range(len(words)):
            word = words[i]
            if word != "":
                if "" in word_dictionary and is_palindrome(word):
                    empty_idx = word_dictionary[""]
                    result.append([i, empty_idx])
                    result.append([empty_idx, i])

                reversed_word = word[::-1]
                if reversed_word in word_dictionary and word_dictionary[reversed_word] != i:
                    result.append([i, word_dictionary[reversed_word]])

                for j in range(1, len(word)):
                    prefix = word[:j]
                    suffix = word[j:]
                    reversed_prefix = prefix[::-1]
                    reversed_suffix = suffix[::-1]

                    if is_palindrome(suffix) and reversed_prefix in word_dictionary:
                        result.append([i, word_dictionary[reversed_prefix]])

                    if is_palindrome(prefix) and reversed_suffix in word_dictionary:
                        result.append([word_dictionary[reversed_suffix], i])

        return result

    def create_word_dictionary(self, words):
        return {word: i for i, word in enumerate(words)}