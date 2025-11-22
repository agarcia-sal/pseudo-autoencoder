class Solution:
    def frequencySort(self, s):
        from collections import Counter

        frequency = self.Counter(s)
        sorted_characters = self.sort_keys_of_frequency_by_descending_frequency(frequency)
        result = self.build_result_string_with_repeated_characters(sorted_characters, frequency)
        return result

    def import_Counter(self):
        from collections import Counter  # This method is not actually used in Python

    def Counter(self, s):
        from collections import Counter
        return Counter(s)

    def sort_keys_of_frequency_by_descending_frequency(self, frequency):
        keys_list = list(frequency.keys())
        keys_list.sort(key=lambda c: frequency[c], reverse=True)
        return keys_list

    def build_result_string_with_repeated_characters(self, sorted_characters, frequency):
        result_string = ''
        for character in sorted_characters:
            repeated_characters = character * frequency[character]
            result_string += repeated_characters
        return result_string