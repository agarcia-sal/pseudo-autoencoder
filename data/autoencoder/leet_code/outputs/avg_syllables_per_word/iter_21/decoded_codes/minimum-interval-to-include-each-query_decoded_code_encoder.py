import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        # Pair each query with its original index and sort by query value
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)], key=lambda x: x[0])

        min_heap = []
        result = [-1] * len(queries)

        interval_index = 0
        for query, original_index in sorted_queries:
            # Add all intervals starting on or before the query to the heap
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                interval_size = end - start + 1
                # Push (interval_size, end) to maintain smallest interval size at the top
                heapq.heappush(min_heap, (interval_size, end))
                interval_index += 1

            # Remove intervals from heap that end before the query (no coverage)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # If there is an interval that covers the query, set its size in result
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result