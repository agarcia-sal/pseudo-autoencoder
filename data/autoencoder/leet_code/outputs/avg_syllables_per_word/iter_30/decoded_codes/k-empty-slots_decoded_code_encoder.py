from bisect import bisect_left

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        bloom_days = []
        day_counter = 1
        for position in bulbs:
            insertion_index = bisect_left(bloom_days, position)
            if insertion_index > 0 and position - bloom_days[insertion_index - 1] - 1 == k:
                return day_counter
            if insertion_index < len(bloom_days) and bloom_days[insertion_index] - position - 1 == k:
                return day_counter
            bloom_days.insert(insertion_index, position)
            day_counter += 1
        return -1