import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo = []  # max heap (store negatives)
        hi = []  # min heap

        def balance_heaps():
            # Balance sizes so that len(lo) == len(hi) or len(lo) == len(hi) + 1
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def add_num(num: int):
            # Add num to appropriate heap
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num: int):
            # Remove num from appropriate heap by searching (linear scan)
            # then heapify to restore heap property
            if lo and num <= -lo[0]:
                # Remove -num from lo
                neg_num = -num
                # Since lo is a heap storing negative nums
                # Search for neg_num and remove it
                for i in range(len(lo)):
                    if lo[i] == neg_num:
                        # remove element at index i
                        lo[i] = lo[-1]
                        lo.pop()
                        if i < len(lo):
                            heapq._siftup(lo, i)
                            heapq._siftdown(lo, 0, i)
                        break
            else:
                # Remove num from hi
                for i in range(len(hi)):
                    if hi[i] == num:
                        hi[i] = hi[-1]
                        hi.pop()
                        if i < len(hi):
                            heapq._siftup(hi, i)
                            heapq._siftdown(hi, 0, i)
                        break
            balance_heaps()

        def get_median():
            if len(lo) > len(hi):
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2.0

        # Initialize the heaps with first k numbers
        for i in range(k):
            add_num(nums[i])

        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians