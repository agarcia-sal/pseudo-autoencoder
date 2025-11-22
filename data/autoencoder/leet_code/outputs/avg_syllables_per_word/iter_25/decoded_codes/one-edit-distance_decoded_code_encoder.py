class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        diff = len(t) - len(s)
        if diff > 1:
            return False
        if diff == 0:
            # Check if exactly one character differs
            return sum(cs != ct for cs, ct in zip(s, t)) == 1
        else:
            # diff == 1
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            # If all previous chars are the same, the only difference is the last extra char in t
            return True