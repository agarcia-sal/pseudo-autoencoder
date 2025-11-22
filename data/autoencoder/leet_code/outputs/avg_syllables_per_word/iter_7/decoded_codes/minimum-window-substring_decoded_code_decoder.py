from collections import Counter
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count: Dict[str, int] = Counter(t)
        required: int = len(t_count)

        left: int = 0
        right: int = 0
        formed: int = 0
        window_counts: Dict[str, int] = {}

        min_length = float("inf")
        min_start = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_start = left

                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == float("inf"):
            return ""
        else:
            return s[min_start : min_start + min_length]