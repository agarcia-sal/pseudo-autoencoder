import heapq
from typing import List, Tuple

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries: List[Tuple[int, int]] = sorted((q, i) for i, q in enumerate(queries))

        min_heap: List[Tuple[int, int]] = []
        result = [-1] * len(queries)

        interval_index = 0
        n = len(intervals)

        for query, original_index in sorted_queries:
            while interval_index < n and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))
                interval_index += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                result[original_index] = min_heap[0][0]

        return result