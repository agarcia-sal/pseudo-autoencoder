from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_of_s = len(s)
        length_of_p = len(p)
        if length_of_p > length_of_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:length_of_p - 1])
        anagrams = []

        for i in range(length_of_p - 1, length_of_s):
            s_count[s[i]] += 1

            start_char = s[i - length_of_p + 1]
            if i - length_of_p >= 0:
                # This check is to ensure index is valid, but here we don't need it
                # because the loop starts at length_of_p - 1, so i-length_of_p +1 >=0.
                pass
            s_count[start_char] -= 1
            if s_count[start_char] == 0:
                del s_count[start_char]

            if s_count == p_count:
                anagrams.append(i - length_of_p + 1)

        return anagrams