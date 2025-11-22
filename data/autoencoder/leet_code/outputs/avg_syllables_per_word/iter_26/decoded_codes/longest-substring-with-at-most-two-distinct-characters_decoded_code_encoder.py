from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        character_count = defaultdict(int)
        left_pointer = 0
        maximum_substring_length = 0

        for right_pointer in range(len(s)):
            character_count[s[right_pointer]] += 1

            while len(character_count) > 2:
                character_count[s[left_pointer]] -= 1
                if character_count[s[left_pointer]] == 0:
                    del character_count[s[left_pointer]]
                left_pointer += 1

            maximum_substring_length = max(maximum_substring_length, right_pointer - left_pointer + 1)

        return maximum_substring_length