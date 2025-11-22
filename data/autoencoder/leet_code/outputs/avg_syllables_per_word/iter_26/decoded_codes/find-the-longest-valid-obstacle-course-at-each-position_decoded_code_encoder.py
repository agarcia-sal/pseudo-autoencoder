from bisect import bisect_right
from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        increasing_subsequence_list = []
        answer_list = []

        for obstacle_element in obstacles:
            found_index = bisect_right(increasing_subsequence_list, obstacle_element)
            if found_index == len(increasing_subsequence_list):
                increasing_subsequence_list.append(obstacle_element)
            else:
                increasing_subsequence_list[found_index] = obstacle_element
            answer_list.append(found_index + 1)

        return answer_list