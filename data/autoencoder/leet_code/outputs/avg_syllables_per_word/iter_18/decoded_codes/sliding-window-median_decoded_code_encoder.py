import heapq

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        lo, hi = [], []

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                popped_value = -heapq.heappop(lo)
                heapq.heappush(hi, popped_value)
            elif len(hi) > len(lo):
                popped_value = heapq.heappop(hi)
                heapq.heappush(lo, -popped_value)

        def add_num(num: int):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int):
            # Remove num from appropriate heap, then heapify
            if num <= -lo[0]:
                lo.remove(-num)
                if lo:
                    heapq.heapify(lo)
            else:
                hi.remove(num)
                if hi:
                    heapq.heapify(hi)
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