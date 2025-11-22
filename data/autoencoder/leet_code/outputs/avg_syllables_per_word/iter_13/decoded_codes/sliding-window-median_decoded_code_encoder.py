import heapq

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        lo = []  # max heap (invert values)
        hi = []  # min heap
        delayed_lo = {}
        delayed_hi = {}

        def prune(heap, delayed):
            while heap and delayed.get(heap[0], 0):
                delayed[heap[0]] -= 1
                if delayed[heap[0]] == 0:
                    del delayed[heap[0]]
                heapq.heappop(heap)

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
                prune(lo, delayed_lo)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)
                prune(hi, delayed_hi)

        def add_num(num: int):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int):
            # Mark num for lazy removal from the appropriate heap
            if num <= -lo[0]:
                delayed_lo[-num] = delayed_lo.get(-num, 0) + 1
                if lo:
                    prune(lo, delayed_lo)
            else:
                delayed_hi[num] = delayed_hi.get(num, 0) + 1
                if hi:
                    prune(hi, delayed_hi)
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
            medians.append(get_median())

        return medians