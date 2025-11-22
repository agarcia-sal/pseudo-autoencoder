from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = Counter(s)
        for ch in count:
            if count[ch] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        return len(s)