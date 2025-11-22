from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, list_of_strings: List[str]) -> List[List[str]]:
        anagrams_mapping = defaultdict(list)
        for string in list_of_strings:
            sorted_string_key = ''.join(sorted(string))
            anagrams_mapping[sorted_string_key].append(string)
        return list(anagrams_mapping.values())