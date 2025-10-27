from bisect import bisect_left, insort

class Solution:
    def kEmptySlots(self, bulbs, k):
        bloom_days = []
        for day, position in enumerate(bulbs, start=1):
            i = bisect_left(bloom_days, position)
            if i > 0 and position - bloom_days[i - 1] - 1 == k:
                return day
            if i < len(bloom_days) and bloom_days[i] - position - 1 == k:
                return day
            insort(bloom_days, position)
        return -1