class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_length_dictionary = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        current_valid_substring_length = 0

        for i in range(len(s)):
            if i > 0 and ((ord(s[i]) - ord(s[i - 1]) == 1) or (s[i] == 'a' and s[i - 1] == 'z')):
                current_valid_substring_length += 1
            else:
                current_valid_substring_length = 1

            max_length_dictionary[s[i]] = max(max_length_dictionary[s[i]], current_valid_substring_length)

        return sum(max_length_dictionary.values())