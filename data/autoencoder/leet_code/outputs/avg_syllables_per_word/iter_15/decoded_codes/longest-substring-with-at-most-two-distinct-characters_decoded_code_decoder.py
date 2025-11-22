from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        character_count = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(s)):
            character_count[s[right]] += 1
            while len(character_count) > 2:
                character_count[s[left]] -= 1
                if character_count[s[left]] == 0:
                    del character_count[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length