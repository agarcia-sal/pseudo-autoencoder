from heapq import heappush, heappop, heapify

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []
        hi = []

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                heappush(hi, -heappop(lo))
            elif len(hi) > len(lo):
                heappush(lo, -heappop(hi))

        def add_num(num):
            if not lo or num <= -lo[0]:
                heappush(lo, -num)
            else:
                heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            if num <= -lo[0]:
                lo.remove(-num)
                if lo:
                    heapify(lo)
            else:
                hi.remove(num)
                if hi:
                    heapify(hi)
            balance_heaps()

        for i in range(k):
            add_num(nums[i])

        medians = [get_median()]

        def get_median():
            if len(lo) > len(hi):
                return float(-lo[0])
            return (float(-lo[0]) + float(hi[0])) / 2

        medians[0] = get_median()

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians