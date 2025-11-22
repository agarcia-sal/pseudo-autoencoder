import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max-heap (inverted values)
        hi = []  # min-heap
        delayed = {}  # counts of elements to remove lazily

        def balance_heaps():
            # Ensure size property lo can have one more element than hi
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def prune(heap):
            # Remove elements marked for deletion at the heap top
            while heap and delayed.get((heap[0] if heap is hi else -heap[0]), 0) > 0:
                val = heap[0] if heap is hi else -heap[0]
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def add_num(num: int):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int):
            delayed[num] = delayed.get(num, 0) + 1
            if lo and num <= -lo[0]:
                # num is in lo heap
                if num == -lo[0]:
                    prune(lo)
            else:
                # num is in hi heap
                if hi and hi[0] == num:
                    prune(hi)
            balance_heaps()
            # After balancing, prune top elements if they are delayed
            prune(lo)
            prune(hi)

        def get_median() -> float:
            if len(lo) > len(hi):
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2.0

        for i in range(k):
            add_num(nums[i])
        medians = [get_median()]
        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())
        return medians