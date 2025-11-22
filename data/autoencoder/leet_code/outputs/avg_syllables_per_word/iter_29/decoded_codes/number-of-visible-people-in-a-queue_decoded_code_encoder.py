from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        number_of_people = len(heights)
        answer_list = [0] * number_of_people
        stack_list = []

        for index in range(number_of_people):
            while stack_list and heights[stack_list[-1]] < heights[index]:
                popped_index = stack_list.pop()
                answer_list[popped_index] += 1
            if stack_list:
                answer_list[stack_list[-1]] += 1
            stack_list.append(index)

        return answer_list