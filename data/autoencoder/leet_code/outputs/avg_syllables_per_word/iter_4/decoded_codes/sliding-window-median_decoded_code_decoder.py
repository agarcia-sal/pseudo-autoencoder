import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []  # max heap (store negative values)
        hi = []  # min heap

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            # Lazy removal: mark removals and actually remove when heap top corresponds
            # However pseudocode removes directly and rebuilds heap.
            # To remove efficiently, we will remove and re-heapify as per pseudocode.
            if num <= -lo[0]:
                # Remove -num from lo
                # Remove first occurrence directly, then heapify
                lo.remove(-num)
                if lo:
                    heapq.heapify(lo)
            else:
                hi.remove(num)
                if hi:
                    heapq.heapify(hi)
            balance_heaps()

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