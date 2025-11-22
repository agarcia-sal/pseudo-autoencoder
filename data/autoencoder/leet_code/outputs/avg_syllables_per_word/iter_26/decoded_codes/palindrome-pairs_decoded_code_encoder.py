class Solution:
    def palindromePairs(self, words):
        def is_palindrome(string_to_check):
            return string_to_check == string_to_check[::-1]

        word_dict = {}
        for index in range(len(words)):
            word_dict[words[index]] = index

        result = []

        for index in range(len(words)):
            word = words[index]

            if word == "":
                continue

            if "" in word_dict and is_palindrome(word):
                result.append([index, word_dict[""]])
                result.append([word_dict[""], index])

            reversed_word = word[::-1]
            if reversed_word in word_dict and word_dict[reversed_word] != index:
                result.append([index, word_dict[reversed_word]])

            for cut_position in range(1, len(word)):
                prefix = word[:cut_position]
                suffix = word[cut_position:]
                reversed_prefix = prefix[::-1]
                reversed_suffix = suffix[::-1]

                if is_palindrome(suffix) and reversed_prefix in word_dict:
                    result.append([index, word_dict[reversed_prefix]])

                if is_palindrome(prefix) and reversed_suffix in word_dict:
                    result.append([word_dict[reversed_suffix], index])

        return result