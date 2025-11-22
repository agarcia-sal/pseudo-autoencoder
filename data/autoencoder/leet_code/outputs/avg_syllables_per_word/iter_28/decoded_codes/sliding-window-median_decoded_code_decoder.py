import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo, hi = [], []
        lo_count, hi_count = Counter(), Counter()
        lo_size, hi_size = 0, 0

        def balance_heaps():
            nonlocal lo_size, hi_size
            if lo_size > hi_size + 1:
                val = -heapq.heappop(lo)
                lo_count[val] -= 1
                hi_count[val] += 1
                heapq.heappush(hi, val)
                lo_size -= 1
                hi_size += 1
                clean_heap(lo, lo_count)
            elif hi_size > lo_size:
                val = heapq.heappop(hi)
                hi_count[val] -= 1
                lo_count[val] += 1
                heapq.heappush(lo, -val)
                hi_size -= 1
                lo_size += 1
                clean_heap(hi, hi_count)

        def add_num(num):
            nonlocal lo_size, hi_size
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
                lo_count[num] += 1
                lo_size += 1
            else:
                heapq.heappush(hi, num)
                hi_count[num] += 1
                hi_size += 1
            balance_heaps()

        def remove_num(num):
            nonlocal lo_size, hi_size
            if lo and num <= -lo[0]:
                lo_count[num] -= 1
                lo_size -= 1
                clean_heap(lo, lo_count)
            else:
                hi_count[num] -= 1
                hi_size -= 1
                clean_heap(hi, hi_count)
            balance_heaps()

        def clean_heap(heap, count_map):
            while heap and count_map[get_val(heap[0])] <= 0:
                heapq.heappop(heap)

        def get_val(heap_item):
            # For lo heap (max heap by negation), val stored is negative
            return -heap_item if heap is lo else heap_item

        def get_median():
            if lo_size > hi_size:
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2

        medians = []
        for i in range(k):
            add_num(nums[i])
        medians.append(get_median())

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians