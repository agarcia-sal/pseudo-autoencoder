import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = [], []  # lo is max heap of inverted values, hi is min heap
        delayed_lo = {}
        delayed_hi = {}

        def balance_heaps():
            # Balance the sizes of the heaps so that len(lo) == len(hi) or len(lo) == len(hi)+1
            while len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                self._add_to_heap(hi, val, delayed_hi)
            while len(hi) > len(lo):
                val = heapq.heappop(hi)
                self._add_to_heap(lo, -val, delayed_lo)
            # Clean up tops that are marked for removal
            self._prune_heap(lo, delayed_lo)
            self._prune_heap(hi, delayed_hi)

        def add_num(num: int):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int):
            # We mark the number as delayed removal and prune heaps if needed
            if lo and num <= -lo[0]:
                delayed_lo[num] = delayed_lo.get(num, 0) + 1
                if num == -lo[0]:
                    self._prune_heap(lo, delayed_lo)
            else:
                delayed_hi[num] = delayed_hi.get(num, 0) + 1
                if hi and num == hi[0]:
                    self._prune_heap(hi, delayed_hi)
            balance_heaps()

        def get_median() -> float:
            if len(lo) > len(hi):
                return float(-lo[0])
            else:
                return ((-lo[0]) + hi[0]) / 2

        for i in range(k):
            add_num(nums[i])
        medians = [get_median()]
        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())
        return medians

    def _add_to_heap(self, heap: List[int], val: int, delayed: dict):
        # Direct push since val is not delayed
        heapq.heappush(heap, val)

    def _prune_heap(self, heap: List[int], delayed: dict):
        # Remove elements at heap top that are delayed for removal
        while heap and delayed.get(abs(heap[0]) if heap is not None else 0, 0) > 0:
            val = heap[0]
            key = val if heap is None else (val if heap is not None else 0)
            # For lo heap val is negative, so get abs
            key = -val if heap is not None and heap[0] < 0 else val
            if delayed.get(key, 0) > 0:
                delayed[key] -= 1
                if delayed[key] == 0:
                    del delayed[key]
                heapq.heappop(heap)
            else:
                break