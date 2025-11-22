class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        min_len = float('inf')
        min_start = -1
        length_of_s1 = len(s1)
        length_of_s2 = len(s2)

        for i in range(length_of_s1):
            j = 0
            for k in range(i, length_of_s1):
                if s1[k] == s2[j]:
                    j += 1
                    if j == length_of_s2:
                        window_len = k - i + 1
                        if window_len < min_len:
                            min_len = window_len
                            min_start = i
                        break

        if min_start == -1:
            return ""
        else:
            return s1[min_start:min_start + min_len]