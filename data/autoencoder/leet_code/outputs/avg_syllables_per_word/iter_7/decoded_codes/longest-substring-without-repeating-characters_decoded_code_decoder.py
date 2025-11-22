from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map: Dict[str, int] = {}
        max_length: int = 0
        start: int = 0

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length