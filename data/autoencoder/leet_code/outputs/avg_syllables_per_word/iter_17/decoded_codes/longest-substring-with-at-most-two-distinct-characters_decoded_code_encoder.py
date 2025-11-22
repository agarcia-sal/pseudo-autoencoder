from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, input_string: str) -> int:
        char_count = defaultdict(int)
        left_pointer = 0
        maximum_length = 0

        for index_pointer in range(len(input_string)):
            char_count[input_string[index_pointer]] += 1

            while len(char_count) > 2:
                left_char = input_string[left_pointer]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left_pointer += 1

            maximum_length = max(maximum_length, index_pointer - left_pointer + 1)

        return maximum_length