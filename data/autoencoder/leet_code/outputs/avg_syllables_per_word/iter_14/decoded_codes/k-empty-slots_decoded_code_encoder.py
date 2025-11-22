from bisect import bisect_left

class Solution:
    def kEmptySlots(self, bulbs, k):
        bloom_days = []
        day = 1
        for position in bulbs:
            i = bisect_left(bloom_days, position)
            if i > 0 and position - bloom_days[i - 1] - 1 == k:
                return day
            if i < len(bloom_days) and bloom_days[i] - position - 1 == k:
                return day
            bloom_days.insert(i, position)
            day += 1
        return -1