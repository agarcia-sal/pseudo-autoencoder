import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        min_heap = []  # will hold end times of meetings currently using rooms

        for meeting in intervals:
            start, end = meeting
            # If a room is free (earliest ending meeting ended before this meeting starts), reuse it
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            # Allocate the current meeting's room (push its end time)
            heapq.heappush(min_heap, end)

        # Number of rooms required is the size of the heap
        return len(min_heap)