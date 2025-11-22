import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo, hi = [], []
        delayed = Counter()

        def balance_heaps():
            # balance sizes
            while len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            while len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def prune_heap(heap):
            while heap and delayed[(-heap[0] if heap is lo else heap[0])] > 0:
                val = -heapq.heappop(heap) if heap is lo else heapq.heappop(heap)
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            delayed[num] += 1
            if num <= -lo[0]:
                if num == -lo[0]:
                    prune_heap(lo)
            else:
                if hi and num == hi[0]:
                    prune_heap(hi)
            balance_heaps()
            prune_heap(lo)
            prune_heap(hi)

        def get_median():
            if k % 2 == 1:
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