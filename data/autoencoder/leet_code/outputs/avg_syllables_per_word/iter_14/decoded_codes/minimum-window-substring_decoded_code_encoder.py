from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        required = len(t_count)

        left = 0
        right = 0
        formed = 0
        window_counts = Counter()

        min_length = float('inf')
        min_start = 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                window_size = right - left + 1
                if window_size < min_length:
                    min_length = window_size
                    min_start = left

                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                left += 1

            right += 1

        if min_length == float('inf'):
            return ""
        else:
            return s[min_start:min_start + min_length]