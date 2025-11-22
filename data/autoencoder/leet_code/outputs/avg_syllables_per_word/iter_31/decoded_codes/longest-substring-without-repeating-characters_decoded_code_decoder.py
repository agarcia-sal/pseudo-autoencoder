from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: Dict[str, int] = {}
        max_length = 0
        start = 0

        for end, character in enumerate(s):
            if character in char_index_map and char_index_map[character] >= start:
                start = char_index_map[character] + 1
            char_index_map[character] = end
            max_length = max(max_length, end - start + 1)

        return max_length