from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for string_element in strs:
            sorted_string = ''.join(sorted(string_element))
            anagrams[sorted_string].append(string_element)
        return list(anagrams.values())