class Solution:
    def findSubstringInWraproundString(self, string_s: str) -> int:
        # Dictionary to keep track of the max length of substrings ending with each character
        max_length_dictionary = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}

        current_length = 0

        for i in range(len(string_s)):
            if i > 0 and (
                ord(string_s[i]) - ord(string_s[i - 1]) == 1 or
                (string_s[i] == 'a' and string_s[i - 1] == 'z')
            ):
                current_length += 1
            else:
                current_length = 1

            key_character = string_s[i]
            current_maximum = max_length_dictionary[key_character]
            if current_length > current_maximum:
                max_length_dictionary[key_character] = current_length

        total_unique_substrings = sum(max_length_dictionary.values())
        return total_unique_substrings