from collections import Counter
from typing import List

class Solution:
    def generatePalindromes(self, string_input: str) -> List[str]:
        def dfs(current_string: str):
            if len(current_string) == len(string_input):
                answer_collection.append(current_string)
                return
            for char_key, char_value in count_dictionary.items():
                if char_value > 1:
                    count_dictionary[char_key] -= 2
                    dfs(char_key + current_string + char_key)
                    count_dictionary[char_key] += 2

        count_dictionary = Counter(string_input)
        middle_character = ''
        for char_key, char_value in count_dictionary.items():
            if char_value % 2 == 1:
                if middle_character != '':
                    return []
                middle_character = char_key
                count_dictionary[char_key] -= 1
        answer_collection = []
        dfs(middle_character)
        return answer_collection