from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, list_of_strings: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string_element in list_of_strings:
            sorted_string = ''.join(sorted(string_element))
            anagrams[sorted_string].append(string_element)
        result_list = list(anagrams.values())
        return result_list