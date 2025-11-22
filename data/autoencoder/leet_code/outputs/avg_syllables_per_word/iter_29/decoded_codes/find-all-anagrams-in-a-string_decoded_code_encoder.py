from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length_of_s = len(s)
        length_of_p = len(p)

        if length_of_p > length_of_s:
            return []

        character_frequency_in_p = Counter(p)
        character_frequency_in_s_window = Counter(s[:length_of_p])

        list_of_starting_indices_of_anagrams = []
        if character_frequency_in_s_window == character_frequency_in_p:
            list_of_starting_indices_of_anagrams.append(0)

        for index in range(length_of_p, length_of_s):
            current_character_to_add = s[index]
            character_frequency_in_s_window[current_character_to_add] += 1

            character_to_remove = s[index - length_of_p]
            character_frequency_in_s_window[character_to_remove] -= 1

            if character_frequency_in_s_window[character_to_remove] == 0:
                del character_frequency_in_s_window[character_to_remove]

            if character_frequency_in_s_window == character_frequency_in_p:
                starting_index = index - length_of_p + 1
                list_of_starting_indices_of_anagrams.append(starting_index)

        return list_of_starting_indices_of_anagrams