from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, list_of_numbers, k):
        def atMostKDistinct(t):
            count_dictionary = defaultdict(int)
            left_pointer = 0
            result_accumulator = 0
            for right_pointer in range(len(list_of_numbers)):
                count_dictionary[list_of_numbers[right_pointer]] += 1
                while len(count_dictionary) > t:
                    count_dictionary[list_of_numbers[left_pointer]] -= 1
                    if count_dictionary[list_of_numbers[left_pointer]] == 0:
                        del count_dictionary[list_of_numbers[left_pointer]]
                    left_pointer += 1
                result_accumulator += right_pointer - left_pointer + 1
            return result_accumulator

        return atMostKDistinct(k) - atMostKDistinct(k - 1)