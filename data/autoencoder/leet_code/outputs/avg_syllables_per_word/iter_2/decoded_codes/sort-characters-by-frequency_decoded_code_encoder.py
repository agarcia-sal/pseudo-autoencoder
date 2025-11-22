from collections import Counter

class Solution:
    def frequencySort(self, s):
        frequency = Counter(s)
        sorted_characters = sorted(frequency.keys(), key=lambda char: frequency[char], reverse=True)
        result = ""
        for char in sorted_characters:
            result += char * frequency[char]
        return result