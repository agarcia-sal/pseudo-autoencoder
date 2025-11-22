class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        min_len = float('inf')
        min_start = -1
        len_s1 = len(s1)
        len_s2 = len(s2)

        for start in range(len_s1):
            pointer_s2 = 0
            for i in range(start, len_s1):
                if s1[i] == s2[pointer_s2]:
                    pointer_s2 += 1
                    if pointer_s2 == len_s2:
                        window_len = i - start + 1
                        if window_len < min_len:
                            min_len = window_len
                            min_start = start
                        break

        if min_start == -1:
            return ""
        else:
            return s1[min_start:min_start + min_len]