import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        for meeting in intervals:
            if min_heap and meeting[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, meeting[1])
        return len(min_heap)