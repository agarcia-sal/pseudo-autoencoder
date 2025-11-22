import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max heap (invert values to use min heap as max heap)
        hi = []  # min heap
        delayed = {}  # counts of elements to be removed lazily
        lo_size = 0  # actual size excluding delayed elements
        hi_size = 0

        def heap_remove(num: int, heap: List[int]):
            delayed[num] = delayed.get(num, 0) + 1

        def prune(heap: List[int]):
            # Remove elements from the top of heap which should be discarded
            while heap:
                val = heap[0]
                # lo is a max heap stored as negatives
                real_val = -val if heap is lo else val
                if delayed.get(real_val, 0):
                    delayed[real_val] -= 1
                    if delayed[real_val] == 0:
                        del delayed[real_val]
                    heapq.heappop(heap)
                else:
                    break

        def balance_heaps():
            nonlocal lo_size, hi_size
            # Balance sizes so that lo_size >= hi_size and size difference <= 1
            if lo_size > hi_size + 1:
                val = -heapq.heappop(lo)
                lo_size -= 1
                heapq.heappush(hi, val)
                hi_size += 1
                prune(lo)
            elif hi_size > lo_size:
                val = heapq.heappop(hi)
                hi_size -= 1
                heapq.heappush(lo, -val)
                lo_size += 1
                prune(hi)

        def add_num(num: int):
            nonlocal lo_size, hi_size
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
                lo_size += 1
            else:
                heapq.heappush(hi, num)
                hi_size += 1
            balance_heaps()

        def remove_num(num: int):
            nonlocal lo_size, hi_size
            # Mark num for delayed removal
            if lo and num <= -lo[0]:
                lo_size -= 1
                heap_remove(num, lo)
                if lo:
                    prune(lo)
            else:
                hi_size -= 1
                heap_remove(num, hi)
                if hi:
                    prune(hi)
            balance_heaps()

        def get_median() -> float:
            if lo_size > hi_size:
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2

        for i in range(k):
            add_num(nums[i])
        medians = [get_median()]
        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())
        return medians