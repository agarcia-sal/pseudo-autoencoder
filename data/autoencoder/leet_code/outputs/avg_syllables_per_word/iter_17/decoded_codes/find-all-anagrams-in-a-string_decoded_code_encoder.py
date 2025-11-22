from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        length_of_string_s = len(s)
        length_of_string_p = len(p)

        if length_of_string_p > length_of_string_s:
            return []

        p_character_counts = Counter(p)
        s_character_counts = Counter(s[:length_of_string_p])

        anagrams_list = []
        if s_character_counts == p_character_counts:
            anagrams_list.append(0)

        for index in range(length_of_string_p, length_of_string_s):
            new_character = s[index]
            s_character_counts[new_character] = s_character_counts.get(new_character, 0) + 1

            old_character = s[index - length_of_string_p]
            s_character_counts[old_character] -= 1
            if s_character_counts[old_character] == 0:
                del s_character_counts[old_character]

            if s_character_counts == p_character_counts:
                anagrams_list.append(index - length_of_string_p + 1)

        return anagrams_list