from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_characters = ''.join(sorted(s))
            anagrams[sorted_characters].append(s)
        return list(anagrams.values())