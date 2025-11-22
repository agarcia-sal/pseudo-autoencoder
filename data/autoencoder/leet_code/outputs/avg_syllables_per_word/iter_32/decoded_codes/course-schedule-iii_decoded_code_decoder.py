import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        self.sort_courses_by_end_day(courses)
        max_heap = []
        current_end_day = 0
        for course in courses:
            duration, last_day = course[0], course[1]
            if current_end_day + duration <= last_day:
                self.push_duration_negated(max_heap, duration)
                current_end_day += duration
            elif max_heap and (-max_heap[0]) > duration:
                # Replace the longest duration course with current shorter duration course
                removed_duration = -heapq.heappop(max_heap)
                current_end_day += duration - removed_duration
                self.push_duration_negated(max_heap, duration)
        return len(max_heap)

    def sort_courses_by_end_day(self, courses: List[List[int]]) -> None:
        courses.sort(key=lambda x: x[1])

    def push_duration_negated(self, max_heap: List[int], duration: int) -> None:
        # Push negative duration to simulate max-heap using heapq (which is min-heap)
        heapq.heappush(max_heap, -duration)