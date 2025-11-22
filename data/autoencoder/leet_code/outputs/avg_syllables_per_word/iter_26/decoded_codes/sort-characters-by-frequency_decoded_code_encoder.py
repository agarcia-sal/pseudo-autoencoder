from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_characters = sorted(frequency, key=lambda c: frequency[c], reverse=True)
        result = ''.join(c * frequency[c] for c in sorted_characters)
        return result