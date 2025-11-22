from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        left = 0
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
            if max_count < count[s[right]]:
                max_count = count[s[right]]

            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            if max_length < right - left + 1:
                max_length = right - left + 1

        return max_length