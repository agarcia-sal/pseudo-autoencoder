import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        lo, hi = [], []
        lo_map, hi_map = {}, {}

        def balance_heaps():
            while len(lo) > len(hi) + 1:
                val = -heapq.heappop(lo)
                while lo_map.get(val, 0):
                    lo_map[val] -= 1
                    val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
            while len(hi) > len(lo):
                val = heapq.heappop(hi)
                while hi_map.get(val, 0):
                    hi_map[val] -= 1
                    val = heapq.heappop(hi)
                heapq.heappush(lo, -val)

        def add_num(num):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            balance_heaps()

        def remove_num(num):
            if num <= -lo[0]:
                lo_map[num] = lo_map.get(num, 0) + 1
                while lo and lo_map.get(-lo[0], 0):
                    val = -heapq.heappop(lo)
                    lo_map[val] -= 1
                    if lo_map[val] == 0:
                        del lo_map[val]
            else:
                hi_map[num] = hi_map.get(num, 0) + 1
                while hi and hi_map.get(hi[0], 0):
                    val = heapq.heappop(hi)
                    hi_map[val] -= 1
                    if hi_map[val] == 0:
                        del hi_map[val]
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