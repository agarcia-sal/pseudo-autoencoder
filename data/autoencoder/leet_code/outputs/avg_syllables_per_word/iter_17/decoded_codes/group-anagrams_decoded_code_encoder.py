from collections import defaultdict

class Solution:
    def groupAnagrams(self, list_of_strings):
        anagrams_dictionary = defaultdict(list)
        for string_element in list_of_strings:
            sorted_characters_list = sorted(string_element)
            sorted_string_key = ''.join(sorted_characters_list)
            anagrams_dictionary[sorted_string_key].append(string_element)
        return list(anagrams_dictionary.values())