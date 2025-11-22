class Solution:
    def isOneEditDistance(self, string_s: str, string_t: str) -> bool:
        if len(string_s) > len(string_t):
            return self.isOneEditDistance(string_t, string_s)

        diff_len = len(string_t) - len(string_s)
        if diff_len > 1:
            return False

        if diff_len == 0:
            diff_count = sum(1 for i in range(len(string_s)) if string_s[i] != string_t[i])
            return diff_count == 1
        else:
            for i in range(len(string_s)):
                if string_s[i] != string_t[i]:
                    return string_s[i:] == string_t[i+1:]
            return True