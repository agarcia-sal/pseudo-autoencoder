import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses by their end day
        courses.sort(key=lambda x: x[1])
        max_heap = []
        current_end_day = 0

        for duration, last_day in courses:
            if current_end_day + duration <= last_day:
                heapq.heappush(max_heap, -duration)
                current_end_day += duration
            elif max_heap and -max_heap[0] > duration:
                # Replace longest duration course with current shorter one
                current_end_day += duration + heapq.heappop(max_heap)  # heapq.heappop returns negative value
                heapq.heappush(max_heap, -duration)

        return len(max_heap)