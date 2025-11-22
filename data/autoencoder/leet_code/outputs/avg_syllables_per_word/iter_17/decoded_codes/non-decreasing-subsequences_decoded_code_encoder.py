from typing import List

class Solution:
    def findSubsequences(self, list_of_numbers: List[int]) -> List[List[int]]:
        answer_list = []
        def dfs(index_position: int, last_number: int, temp_list: List[int]) -> None:
            if index_position == len(list_of_numbers):
                if len(temp_list) > 1:
                    answer_list.append(temp_list.copy())
                return
            current_num = list_of_numbers[index_position]
            if current_num >= last_number:
                temp_list.append(current_num)
                dfs(index_position + 1, current_num, temp_list)
                temp_list.pop()
            if current_num != last_number:
                dfs(index_position + 1, last_number, temp_list)
        dfs(0, -1000, [])
        return answer_list