from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        def key_function(x):
            return frequency[x]
        sorted_characters = sorted(frequency.keys(), key=key_function, reverse=True)
        result = ''.join(char * frequency[char] for char in sorted_characters)
        return result