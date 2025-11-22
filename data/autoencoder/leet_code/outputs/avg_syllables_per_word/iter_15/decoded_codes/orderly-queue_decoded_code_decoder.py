class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        else:
            n = len(s)
            smallest = s
            for index in range(1, n):
                rotated = s[index:] + s[:index]
                if rotated < smallest:
                    smallest = rotated
            return smallest