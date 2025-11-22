import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = [], []
        delayed_lo = {}
        delayed_hi = {}

        def balance_heaps():
            # Balance sizes so that len(lo) == len(hi) or len(lo) == len(hi) + 1
            while len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
                prune(lo, delayed_lo)
            while len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)
                prune(hi, delayed_hi)

        def prune(heap, delayed):
            # Remove from heap top elements that should be deleted (lazy removal)
            while heap and delayed.get((heap[0] if heap is hi else -heap[0]), 0):
                val = heap[0] if heap is hi else -heap[0]
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def add_num(num):
            # Push num to appropriate heap
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            # Lazy removal: mark num to be removed later
            target_heap = lo if num <= -lo[0] else hi
            delayed = delayed_lo if target_heap is lo else delayed_hi
            delayed[num] = delayed.get(num, 0) + 1
            # Physically remove top if it's scheduled
            prune(target_heap, delayed)
            balance_heaps()

        def get_median():
            if k % 2:
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