from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        anagrams = []

        if s_count == p_count:
            anagrams.append(0)

        for i in range(len_p, len_s):
            s_count[s[i]] += 1
            left_char = s[i - len_p]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

            if s_count == p_count:
                anagrams.append(i - len_p + 1)

        return anagrams