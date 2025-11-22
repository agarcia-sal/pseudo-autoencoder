class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(length: int) -> str:
            seen = set()
            for start in range(len(s) - length + 1):
                substring = s[start:start + length]
                if substring in seen:
                    return substring
                seen.add(substring)
            return ""

        left, right = 1, len(s) - 1
        longest = ""

        while left <= right:
            mid = (left + right) // 2
            candidate = search(mid)
            if candidate != "":
                longest = candidate
                left = mid + 1
            else:
                right = mid - 1

        return longest