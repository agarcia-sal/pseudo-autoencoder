import heapq

class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])  # sort by end day ascending
        max_heap = []
        current_end_day = 0
        for duration, last_day in courses:
            if current_end_day + duration <= last_day:
                heapq.heappush(max_heap, -duration)
                current_end_day += duration
            elif max_heap and -max_heap[0] > duration:
                current_end_day += duration + heapq.heappop(max_heap)
                heapq.heappush(max_heap, -duration)
        return len(max_heap)