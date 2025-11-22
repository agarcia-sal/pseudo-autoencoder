from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_of_s = len(s)
        length_of_p = len(p)

        if length_of_p > length_of_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:length_of_p])

        anagrams = []
        if s_count == p_count:
            anagrams.append(0)

        for i in range(length_of_p, length_of_s):
            s_count[s[i]] += 1
            left_char = s[i - length_of_p]
            s_count[left_char] -= 1

            if s_count[left_char] == 0:
                del s_count[left_char]

            if s_count == p_count:
                anagrams.append(i - length_of_p + 1)

        return anagrams