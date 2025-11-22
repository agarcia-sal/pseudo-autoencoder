class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        diff_len = len(t) - len(s)
        if diff_len > 1:
            return False

        if diff_len == 0:
            diff_count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1
        else:
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True