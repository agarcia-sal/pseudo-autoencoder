from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        char_count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length