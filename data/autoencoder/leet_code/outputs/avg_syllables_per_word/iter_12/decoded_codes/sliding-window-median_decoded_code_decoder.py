import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo, hi = [], []  # max-heap (inverted values), min-heap

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                popped_value = -heapq.heappop(lo)
                heapq.heappush(hi, popped_value)
            elif len(hi) > len(lo):
                popped_value = heapq.heappop(hi)
                heapq.heappush(lo, -popped_value)

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            # Decide which heap contains the num based on median comparison
            if num <= -lo[0]:
                # Remove from lo
                # Since heaps do not support removal by value efficiently, remove by rebuilding
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
            return (-lo[0] + hi[0]) / 2

        for i in range(k):
            add_num(nums[i])
        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians