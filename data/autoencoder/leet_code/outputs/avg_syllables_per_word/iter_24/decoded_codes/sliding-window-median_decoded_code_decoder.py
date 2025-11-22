import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max heap (invert values)
        hi = []  # min heap
        delayed = {}

        def balance_heaps() -> None:
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def prune(heap: List[int]) -> None:
            while heap and delayed.get(abs(heap[0]), 0) > 0:
                val = abs(heap[0])
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def add_num(num: int) -> None:
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int) -> None:
            delayed[num] = delayed.get(num, 0) + 1
            if lo and num <= -lo[0]:
                # num is in lo
                if lo:
                    prune(lo)
            else:
                # num is in hi
                if hi:
                    prune(hi)
            balance_heaps()

        def get_median() -> float:
            if len(lo) > len(hi):
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2

        for i in range(k):
            add_num(nums[i])
        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            prune(lo)
            prune(hi)
            medians.append(get_median())

        return medians