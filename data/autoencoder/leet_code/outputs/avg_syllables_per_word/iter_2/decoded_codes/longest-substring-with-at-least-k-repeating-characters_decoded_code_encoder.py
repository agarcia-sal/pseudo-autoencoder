class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in count:
            if count[char] < k:
                results = []
                for substring in s.split(char):
                    results.append(self.longestSubstring(substring, k))
                return max(results)

        return len(s)