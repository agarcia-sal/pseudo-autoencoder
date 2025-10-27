from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        reference = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            reference[s[right]] += 1

            while len(reference) > 2:
                reference[s[left]] -= 1
                if reference[s[left]] == 0:
                    del reference[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length