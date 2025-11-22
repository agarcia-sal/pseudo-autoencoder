from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:len_p - 1])
        anagrams = []

        for i in range(len_p - 1, len_s):
            s_count[s[i]] += 1  # include new char in the window
            start_char = s[i - len_p + 1]
            if s_count == p_count:
                anagrams.append(i - len_p + 1)
            s_count[start_char] -= 1  # remove the oldest char in the window
            if s_count[start_char] == 0:
                del s_count[start_char]

        return anagrams