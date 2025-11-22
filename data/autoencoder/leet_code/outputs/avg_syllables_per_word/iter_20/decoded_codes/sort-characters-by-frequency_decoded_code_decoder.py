from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_characters = sorted(frequency, key=frequency.get, reverse=True)
        result = ''.join(ch * frequency[ch] for ch in sorted_characters)
        return result