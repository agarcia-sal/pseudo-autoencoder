from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mapping = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            mapping[s[right]] += 1

            while len(mapping) > 2:
                mapping[s[left]] -= 1
                if mapping[s[left]] == 0:
                    del mapping[s[left]]
                left += 1

            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length

        return max_length