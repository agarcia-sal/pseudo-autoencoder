class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        diff = len(t) - len(s)
        if diff > 1:
            return False

        if diff == 0:
            # Count number of differing characters; must be exactly one
            count_diff = sum(cs != ct for cs, ct in zip(s, t))
            return count_diff == 1
        else:
            # diff == 1
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            # All previous characters matched; the only difference is an extra char at the end of t
            return True