class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length: int) -> str:
            seen = set()
            for i in range(len(s) - length + 1):
                substr = s[i:i+length]
                if substr in seen:
                    return substr
                seen.add(substr)
            return ""

        left, right = 1, len(s) - 1
        longest = ""
        while left <= right:
            mid = (left + right) // 2
            candidate = search(mid)
            if candidate:
                longest = candidate
                left = mid + 1
            else:
                right = mid - 1
        return longest