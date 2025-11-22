import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max heap (invert values to use Python's min heap)
        hi = []  # min heap

        def balance_heaps() -> None:
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def add_num(num: int) -> None:
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int) -> None:
            # Remove num from either heap, then heapify
            # Since heaps don't support efficient arbitrary removal,
            # we do a linear search and remove the element, then heapify.
            target_heap = lo if num <= -lo[0] else hi
            val_to_remove = -num if target_heap is lo else num
            # Find and remove element
            for i in range(len(target_heap)):
                if target_heap[i] == val_to_remove:
                    target_heap[i] = target_heap[-1]
                    target_heap.pop()
                    if i < len(target_heap):
                        heapq._siftup(target_heap, i)
                        heapq._siftdown(target_heap, 0, i)
                    break
            balance_heaps()

        def get_median() -> float:
            if len(lo) > len(hi):
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2

        for i in range(k):
            add_num(nums[i])

        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians