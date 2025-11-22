import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo, hi = [], []
        delayed = defaultdict(int)

        def balance_heaps():
            while lo and delayed[-lo[0]] > 0:
                delayed[-lo[0]] -= 1
                heapq.heappop(lo)
            while hi and delayed[hi[0]] > 0:
                delayed[hi[0]] -= 1
                heapq.heappop(hi)
            if len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
            elif len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))

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
                    balance_heaps()
            else:
                if hi and num == hi[0]:
                    balance_heaps()
            balance_heaps()

        def get_median():
            if len(lo) > len(hi):
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