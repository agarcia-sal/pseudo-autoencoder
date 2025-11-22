from bisect import bisect_left

class Solution:
    def kEmptySlots(self, bulbs, k):
        list_of_bloom_days = []
        for day, position in enumerate(bulbs, start=1):
            insertion_index = bisect_left(list_of_bloom_days, position)
            if insertion_index > 0 and position - list_of_bloom_days[insertion_index - 1] - 1 == k:
                return day
            if insertion_index < len(list_of_bloom_days) and list_of_bloom_days[insertion_index] - position - 1 == k:
                return day
            list_of_bloom_days.insert(insertion_index, position)
        return -1