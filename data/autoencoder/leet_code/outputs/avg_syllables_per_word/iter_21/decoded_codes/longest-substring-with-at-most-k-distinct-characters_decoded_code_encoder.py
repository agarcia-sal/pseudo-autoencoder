class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_map = dict()
        left = 0
        max_length = 0

        for right in range(len(s)):
            char_map[s[right]] = right

            if len(char_map) > k:
                leftmost_char = min(char_map, key=char_map.get)
                left = char_map[leftmost_char] + 1
                del char_map[leftmost_char]

            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length

        return max_length