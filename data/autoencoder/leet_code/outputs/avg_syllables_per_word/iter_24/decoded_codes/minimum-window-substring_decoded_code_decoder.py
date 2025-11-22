from collections import Counter, defaultdict
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        required = len(t_count)
        left = 0
        right = 0
        formed = 0
        window_counts = defaultdict(int)
        min_length = inf
        min_start = 0

        while right < len(s):
            current_character = s[right]
            window_counts[current_character] += 1

            if current_character in t_count and window_counts[current_character] == t_count[current_character]:
                formed += 1

            while left <= right and formed == required:
                character_to_remove = s[left]
                window_size = right - left + 1

                if window_size < min_length:
                    min_length = window_size
                    min_start = left

                window_counts[character_to_remove] -= 1
                if character_to_remove in t_count and window_counts[character_to_remove] < t_count[character_to_remove]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == inf:
            return ""
        else:
            return s[min_start:min_start + min_length]