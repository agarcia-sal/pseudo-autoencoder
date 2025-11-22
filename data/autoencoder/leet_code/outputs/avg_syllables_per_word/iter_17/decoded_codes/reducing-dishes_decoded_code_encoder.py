from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction_list: List[int]) -> int:
        satisfaction_list.sort(reverse=True)
        max_satisfaction = 0
        current_satisfaction = 0
        total_satisfaction = 0
        for satisfaction_value in satisfaction_list:
            current_satisfaction += satisfaction_value
            total_satisfaction += current_satisfaction
            if total_satisfaction > max_satisfaction:
                max_satisfaction = total_satisfaction
        return max_satisfaction