import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        min_heap = []

        for meeting in intervals:
            # If the earliest ending meeting is done before the current meeting starts, reuse that room
            if min_heap and meeting[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            # Add the current meeting's end time to the heap
            heapq.heappush(min_heap, meeting[1])

        return len(min_heap)