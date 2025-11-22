from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] += 1

            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len