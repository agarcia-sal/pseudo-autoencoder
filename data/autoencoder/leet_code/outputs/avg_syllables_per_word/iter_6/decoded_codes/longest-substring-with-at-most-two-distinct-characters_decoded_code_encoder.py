class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > 2:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length