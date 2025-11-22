class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        else:
            smallest = s
            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest