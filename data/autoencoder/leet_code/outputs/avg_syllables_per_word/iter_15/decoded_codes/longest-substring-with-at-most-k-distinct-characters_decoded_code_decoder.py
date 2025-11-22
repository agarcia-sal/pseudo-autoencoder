class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_map = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            char_map[char] = right

            if len(char_map) > k:
                leftmost_char = min(char_map, key=char_map.get)
                left = char_map[leftmost_char] + 1
                del char_map[leftmost_char]

            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length

        return max_length