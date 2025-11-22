class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in count:
            if count[char] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        return len(s)