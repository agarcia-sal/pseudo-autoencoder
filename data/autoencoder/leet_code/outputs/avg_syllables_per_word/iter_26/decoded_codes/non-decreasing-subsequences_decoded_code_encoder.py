from typing import List

class Solution:
    def findSubsequences(self, list_of_numbers: List[int]) -> List[List[int]]:
        answer_list = []

        def dfs(current_index: int, previous_number: int, temporary_list: List[int]):
            if current_index == len(list_of_numbers):
                if len(temporary_list) > 1:
                    answer_list.append(temporary_list.copy())
                return

            current_num = list_of_numbers[current_index]

            if current_num >= previous_number:
                temporary_list.append(current_num)
                dfs(current_index + 1, current_num, temporary_list)
                temporary_list.pop()

            # Skip duplicates by checking current_num != previous_number before skipping
            if current_num != previous_number:
                dfs(current_index + 1, previous_number, temporary_list)

        dfs(0, -1000, [])
        return answer_list