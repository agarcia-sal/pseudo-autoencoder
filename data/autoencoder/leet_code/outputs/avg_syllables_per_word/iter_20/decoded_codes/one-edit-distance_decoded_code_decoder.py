class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        diff = len(t) - len(s)
        if diff > 1:
            return False

        if diff == 0:
            count_diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count_diff += 1
                    if count_diff > 1:
                        return False
            return count_diff == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True