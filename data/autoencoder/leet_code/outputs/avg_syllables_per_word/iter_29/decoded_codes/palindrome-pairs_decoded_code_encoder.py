class Solution:
    def palindromePairs(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        word_dictionary = {word: i for i, word in enumerate(words)}
        result = []

        for index, word in enumerate(words):
            if word == "":
                continue

            if "" in word_dictionary and is_palindrome(word):
                empty_index = word_dictionary[""]
                result.append([index, empty_index])
                result.append([empty_index, index])

            reversed_word = word[::-1]
            if reversed_word in word_dictionary and word_dictionary[reversed_word] != index:
                result.append([index, word_dictionary[reversed_word]])

            for partition_index in range(1, len(word)):
                prefix = word[:partition_index]
                suffix = word[partition_index:]
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]

                if is_palindrome(suffix) and reversed_prefix in word_dictionary:
                    result.append([index, word_dictionary[reversed_prefix]])

                if is_palindrome(prefix) and reversed_suffix in word_dictionary:
                    result.append([word_dictionary[reversed_suffix], index])

        return result