class Solution:
    def frequencySort(self, s):
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        sorted_characters = sorted(frequency.keys(), key=lambda c: frequency[c], reverse=True)
        result = ""
        for char in sorted_characters:
            result += char * frequency[char]
        return result