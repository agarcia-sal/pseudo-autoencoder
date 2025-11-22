from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_characters = sorted(frequency, key=frequency.get, reverse=True)
        return ''.join(char * frequency[char] for char in sorted_characters)