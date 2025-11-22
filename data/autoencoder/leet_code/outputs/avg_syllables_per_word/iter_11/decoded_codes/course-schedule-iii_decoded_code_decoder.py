from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        max_heap = []
        current_end_day = 0

        for course in courses:
            duration, last_day = course
            if current_end_day + duration <= last_day:
                heappush(max_heap, -duration)
                current_end_day += duration
            else:
                if max_heap and -max_heap[0] > duration:
                    current_end_day += duration + heappop(max_heap)
                    heappush(max_heap, -duration)

        return len(max_heap)