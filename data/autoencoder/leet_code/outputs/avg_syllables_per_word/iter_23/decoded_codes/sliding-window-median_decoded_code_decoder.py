import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo = []  # max heap (as min heap with negated values)
        hi = []  # min heap

        def balance_heaps():
            if len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            elif len(hi) > len(lo):
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        # Remove num from the specified heap and rebalance
        # Because Python heaps do not support arbitrary removal,
        # we remove by locating the element, removing it,
        # and then heapifying again.
        def remove_from_heap(heap, value):
            # heap is a list used as a heap, value is the element to remove
            # This is O(n), but k<=len(nums) and under 5s runtime limit this is acceptable.
            idx = None
            for i, v in enumerate(heap):
                if v == value:
                    idx = i
                    break
            if idx is not None:
                # Remove the element at idx
                heap[idx] = heap[-1]
                heap.pop()
                if idx < len(heap):
                    heapq._siftup(heap, idx)
                    heapq._siftdown(heap, 0, idx)

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            if num <= -lo[0]:
                remove_from_heap(lo, -num)
                if lo:
                    heapq.heapify(lo)
            else:
                remove_from_heap(hi, num)
                if hi:
                    heapq.heapify(hi)
            balance_heaps()

        def get_median():
            if len(lo) > len(hi):
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2.0

        for i in range(k):
            add_num(nums[i])

        medians = [get_median()]

        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            medians.append(get_median())

        return medians