from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_characters = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        result = ""
        for character in sorted_characters:
            result += character * frequency[character]
        return result