class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            # With k > 1, we can permute the string arbitrarily,
            # so sorted string is the smallest lex order.
            return ''.join(sorted(s))
        else:
            n = len(s)
            smallest = s
            for i in range(1, n):
                # Rotate s by i characters
                rotated = s[i:] + s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest