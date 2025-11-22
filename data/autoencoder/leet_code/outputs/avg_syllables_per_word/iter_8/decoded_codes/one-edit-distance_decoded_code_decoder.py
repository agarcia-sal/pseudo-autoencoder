class Solution:
    def isOneEditDistance(self, s, t):
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
            return count == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True