import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], query_list: List[int]) -> List[int]:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        # Pair each query with its original index and sort by the query value
        sorted_queries = sorted((q, i) for i, q in enumerate(query_list))

        min_heap = []
        result = [-1] * len(query_list)
        interval_index = 0
        n = len(intervals)

        for query, original_index in sorted_queries:
            # Push all intervals starting before or at query into the min heap by their size
            while interval_index < n and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                interval_size = end - start + 1
                heapq.heappush(min_heap, (interval_size, end))
                interval_index += 1

            # Remove intervals that end before the query (they don't cover the query)
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # If there is any interval covering the query, the smallest one is at the top of the heap
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result