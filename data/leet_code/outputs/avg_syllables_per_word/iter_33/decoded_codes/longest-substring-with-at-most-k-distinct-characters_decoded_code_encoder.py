class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_map = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            char_map[char] = right  # update rightmost position of char

            if len(char_map) > k:
                # find the leftmost character by minimum position
                leftmost_char = min(char_map, key=char_map.get)
                left = char_map[leftmost_char] + 1
                del char_map[leftmost_char]

            max_length = max(max_length, right - left + 1)

        return max_length