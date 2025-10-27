class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        diff = len(t) - len(s)
        if diff > 1:
            return False

        if diff == 0:
            count = 0
            for c1, c2 in zip(s, t):
                if c1 != c2:
                    count += 1
                    if count > 1:
                        return False
            return count == 1
        else:
            # diff == 1
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True