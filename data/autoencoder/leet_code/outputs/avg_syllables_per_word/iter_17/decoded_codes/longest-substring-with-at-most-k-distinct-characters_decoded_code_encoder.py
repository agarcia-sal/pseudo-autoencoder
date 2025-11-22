class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_map = {}
        left = 0
        max_length = 0

        for right, current_char in enumerate(s):
            char_map[current_char] = right

            if len(char_map) > k:
                leftmost_char = min(char_map, key=char_map.get)
                left = char_map[leftmost_char] + 1
                del char_map[leftmost_char]

            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length