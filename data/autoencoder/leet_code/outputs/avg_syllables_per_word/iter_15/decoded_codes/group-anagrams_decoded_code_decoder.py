from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            characters_in_s = list(s)
            sorted_characters = sorted(characters_in_s)
            sorted_str = ''.join(sorted_characters)
            anagrams[sorted_str].append(s)
        result = list(anagrams.values())
        return result