from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_s = len(s)
        len_p = len(p)
        if len_p > len_s:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:len_p])

        anagrams = []
        if s_count == p_count:
            anagrams.append(0)

        for index in range(len_p, len_s):
            new_character = s[index]
            s_count[new_character] += 1

            old_character = s[index - len_p]
            s_count[old_character] -= 1
            if s_count[old_character] == 0:
                del s_count[old_character]

            if s_count == p_count:
                anagrams.append(index - len_p + 1)

        return anagrams