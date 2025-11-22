from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(time: str) -> int:
            hours, minutes = time.split(':')
            return int(hours) * 60 + int(minutes)

        minutes_list = [to_minutes(time) for time in timePoints]
        minutes_list.sort()

        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i - 1]
            if diff < min_diff:
                min_diff = diff

        circular_difference = 1440 - minutes_list[-1] + minutes_list[0]
        if circular_difference < min_diff:
            min_diff = circular_difference

        return min_diff