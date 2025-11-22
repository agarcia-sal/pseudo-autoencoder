from bisect import bisect_left

class Solution:
    def kEmptySlots(self, bulbs, k):
        bloom_days = []
        for day, position in enumerate(bulbs, 1):
            insertion_index = bisect_left(bloom_days, position)
            if insertion_index > 0 and position - bloom_days[insertion_index - 1] - 1 == k:
                return day
            if insertion_index < len(bloom_days) and bloom_days[insertion_index] - position - 1 == k:
                return day
            bloom_days.insert(insertion_index, position)
        return -1