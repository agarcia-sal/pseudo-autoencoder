from collections import Counter
from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        required = len(t_count)

        left = 0
        right = 0
        formed = 0
        window_counts = Counter()

        min_length = inf
        min_start = 0

        while right < len(s):
            current_character = s[right]
            window_counts[current_character] += 1

            if current_character in t_count and window_counts[current_character] == t_count[current_character]:
                formed += 1

            while left <= right and formed == required:
                character_at_left = s[left]

                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_start = left

                window_counts[character_at_left] -= 1

                if character_at_left in t_count and window_counts[character_at_left] < t_count[character_at_left]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == inf:
            return ""
        else:
            return s[min_start:min_start + min_length]