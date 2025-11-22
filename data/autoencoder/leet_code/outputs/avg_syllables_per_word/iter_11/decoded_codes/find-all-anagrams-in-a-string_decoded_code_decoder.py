from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_s = len(s)
        len_p = len(p)

        if len_p > len_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:len_p-1])

        anagrams = []

        for i in range(len_p - 1, len_s):
            s_count[s[i]] += 1

            if i - len_p >= 0:
                s_count[s[i - len_p]] -= 1
                if s_count[s[i - len_p]] == 0:
                    del s_count[s[i - len_p]]

            if s_count == p_count:
                anagrams.append(i - len_p + 1)

        return anagrams