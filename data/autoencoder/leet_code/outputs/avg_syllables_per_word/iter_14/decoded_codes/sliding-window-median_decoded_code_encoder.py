import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []  # max heap (invert values)
        hi = []  # min heap
        delayed = Counter()  # counts of elements to be removed

        def balance_heaps():
            # Balance the sizes of two heaps so that:
            # len(lo) >= len(hi) and the difference <= 1
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def prune(heap):
            # Remove elements that are marked for deletion from heap top
            while heap and delayed.get(get_heap_val(heap), 0):
                val = get_heap_val(heap)
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def get_heap_val(heap):
            return -heap[0] if heap is lo else heap[0]

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            delayed[num] += 1
            # Remove element logically first, clean from heap tops later
            if lo and num <= -lo[0]:
                # num is in lo heap
                if lo:
                    prune(lo)
            else:
                # num is in hi heap
                if hi:
                    prune(hi)
            balance_heaps()
            # After balancing, prune tops again if needed
            prune(lo)
            prune(hi)

        def get_median():
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