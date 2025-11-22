from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        char_map = OrderedDict()
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_map:
                del char_map[char]
            char_map[char] = right

            if len(char_map) > k:
                _, leftmost_index = char_map.popitem(last=False)
                left = leftmost_index + 1

            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length

        return max_length