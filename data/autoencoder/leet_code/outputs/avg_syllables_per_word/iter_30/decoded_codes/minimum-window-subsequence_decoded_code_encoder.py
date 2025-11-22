class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        min_len = float('inf')
        min_start = -1
        len1 = len(s1)
        len2 = len(s2)
        for i in range(len1):
            j = 0
            for k in range(i, len1):
                if s1[k] == s2[j]:
                    j += 1
                    if j == len2:
                        window_len = k - i + 1
                        if window_len < min_len:
                            min_len = window_len
                            min_start = i
                        break
        if min_start == -1:
            return ""
        else:
            return s1[min_start:min_start + min_len]