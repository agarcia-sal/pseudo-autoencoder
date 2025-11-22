import heapq
from typing import List, Tuple

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Sort workers by their wage-to-quality ratio
        workers = self.sort_ratio_quality(wage, quality)
        max_heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            # Push negative quality because heapq is a min-heap by default
            self.push_element(-q, max_heap)
            total_quality += q

            if len(max_heap) > k:
                total_quality += self.pop_element(max_heap)  # pop_element returns negative, so add to total_quality

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost

    def sort_ratio_quality(self, wage_list: List[int], quality_list: List[int]) -> List[Tuple[float, int]]:
        return sorted(self.generate_ratio_quality_pairs(wage_list, quality_list))

    def generate_ratio_quality_pairs(self, wage_list: List[int], quality_list: List[int]) -> List[Tuple[float, int]]:
        # Each pair is (wage / quality, quality)
        return [(w / q, q) for w, q in zip(wage_list, quality_list)]

    def push_element(self, element: int, heap: List[int]) -> None:
        heapq.heappush(heap, element)

    def pop_element(self, heap: List[int]) -> int:
        return heapq.heappop(heap)