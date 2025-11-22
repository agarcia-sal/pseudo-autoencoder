import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max heap (store negative values)
        hi = []  # min heap
        delayed_lo = {}
        delayed_hi = {}

        def heap_add(heap, delayed, val):
            heapq.heappush(heap, val)

        def heap_remove(heap, delayed, val):
            delayed[val] = delayed.get(val, 0) + 1

        def prune(heap, delayed):
            while heap and delayed.get(heap[0], 0):
                val = heap[0]
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def balance_heaps():
            # Balance sizes: lo can have at most 1 more element than hi
            if len(lo) > len(hi) + 1:
                prune(lo, delayed_lo)
                val = -heapq.heappop(lo)
                heap_add(hi, delayed_hi, val)
            elif len(hi) > len(lo):
                prune(hi, delayed_hi)
                val = heapq.heappop(hi)
                heap_add(lo, delayed_lo, -val)

        def add_num(num: int):
            if not lo or num <= -lo[0]:
                heap_add(lo, delayed_lo, -num)
            else:
                heap_add(hi, delayed_hi, num)
            balance_heaps()

        def remove_num(num: int):
            # Determine which heap the number is in by comparing to lo[0]
            if num <= -lo[0]:
                heap_remove(lo, delayed_lo, -num)
                prune(lo, delayed_lo)
            else:
                heap_remove(hi, delayed_hi, num)
                prune(hi, delayed_hi)
            balance_heaps()

        def get_median() -> float:
            prune(lo, delayed_lo)
            prune(hi, delayed_hi)
            if len(lo) > len(hi):
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2.0

        for i in range(k):
            add_num(nums[i])

        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians