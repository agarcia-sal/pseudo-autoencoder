import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []  # max heap (as negatives)
        hi = []  # min heap
        delayed = Counter()  # counts of elements to be removed
        lo_size = 0  # number of valid elements in lo
        hi_size = 0  # number of valid elements in hi

        def prune(heap):
            while heap and delayed[heap[0] if heap is hi else -heap[0]]:
                val = heap[0] if heap is hi else -heap[0]
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def balance_heaps():
            nonlocal lo_size, hi_size
            # Ensure lo has size >= hi, and difference <= 1
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

        def add_num(num):
            nonlocal lo_size, hi_size
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
                lo_size += 1
            else:
                heapq.heappush(hi, num)
                hi_size += 1
            balance_heaps()

        def remove_num(num):
            nonlocal lo_size, hi_size
            # Mark num as delayed for lazy removal
            delayed[num] += 1
            # Adjust sizes for where num falls
            if lo and num <= -lo[0]:
                lo_size -= 1
                if lo_size < 0:
                    lo_size = 0
                # prune might be needed when next heap pop
                if lo:
                    prune(lo)
            else:
                hi_size -= 1
                if hi_size < 0:
                    hi_size = 0
                if hi:
                    prune(hi)
            balance_heaps()

        def get_median():
            if lo_size > hi_size:
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