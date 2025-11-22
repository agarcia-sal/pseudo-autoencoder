import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses by their last_day (deadline)
        courses.sort(key=lambda x: x[1])

        max_heap = []
        current_end_day = 0

        for duration, last_day in courses:
            if current_end_day + duration <= last_day:
                heapq.heappush(max_heap, -duration)
                current_end_day += duration
            elif max_heap and (-max_heap[0]) > duration:
                # Remove the longest duration course taken so far and add the current one
                current_end_day += duration + heapq.heappop(max_heap)  # heap pop returns negative max duration
                heapq.heappush(max_heap, -duration)

        return len(max_heap)