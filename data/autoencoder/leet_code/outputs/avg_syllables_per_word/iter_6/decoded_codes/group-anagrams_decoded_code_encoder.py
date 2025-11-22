from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())