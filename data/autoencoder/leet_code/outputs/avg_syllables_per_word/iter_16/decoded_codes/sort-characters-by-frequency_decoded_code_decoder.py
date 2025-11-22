from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_characters = sorted(frequency.keys(), key=lambda c: frequency[c], reverse=True)
        result = []
        for character in sorted_characters:
            result.append(character * frequency[character])
        return ''.join(result)