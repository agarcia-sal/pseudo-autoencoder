class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        diff = len(t) - len(s)

        if diff > 1:
            return False

        if diff == 0:
            mismatch_count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    mismatch_count += 1
            return mismatch_count == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True