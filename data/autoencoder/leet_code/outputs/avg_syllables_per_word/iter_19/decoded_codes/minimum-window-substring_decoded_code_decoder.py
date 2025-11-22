from collections import Counter, defaultdict
import math

class Solution:
    def minWindow(self, s, t):
        t_count = Counter(t)
        required = len(t_count)
        left = 0
        right = 0
        formed = 0
        window_counts = defaultdict(int)
        min_length = math.inf
        min_start = 0

        while right < len(s):
            char_right = s[right]
            window_counts[char_right] += 1

            if char_right in t_count and window_counts[char_right] == t_count[char_right]:
                formed += 1

            while left <= right and formed == required:
                char_left = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_start = left

                window_counts[char_left] -= 1
                if char_left in t_count and window_counts[char_left] < t_count[char_left]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == math.inf:
            return ""
        else:
            return s[min_start:min_start + min_length]