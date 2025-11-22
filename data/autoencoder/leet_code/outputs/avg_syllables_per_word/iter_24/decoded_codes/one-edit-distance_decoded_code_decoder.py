class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        diff = len(t) - len(s)
        if diff > 1:
            return False
        if diff == 0:
            return sum(c1 != c2 for c1, c2 in zip(s, t)) == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i + 1:]
            return True