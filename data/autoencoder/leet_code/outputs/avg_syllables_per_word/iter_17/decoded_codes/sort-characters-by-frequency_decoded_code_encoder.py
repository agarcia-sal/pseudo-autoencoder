from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map = Counter(s)
        sorted_characters = sorted(frequency_map.keys(), key=lambda c: frequency_map[c], reverse=True)
        result_string = ''.join(c * frequency_map[c] for c in sorted_characters)
        return result_string