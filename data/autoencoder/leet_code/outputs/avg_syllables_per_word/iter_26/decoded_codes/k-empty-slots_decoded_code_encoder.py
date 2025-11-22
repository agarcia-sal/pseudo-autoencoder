from bisect import bisect_left

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        bloom_days = []
        for day_with_index in range(1, len(bulbs) + 1):
            position = bulbs[day_with_index - 1]
            insertion_index = bisect_left(bloom_days, position)

            if insertion_index > 0 and position - bloom_days[insertion_index - 1] - 1 == k:
                return day_with_index
            if insertion_index < len(bloom_days) and bloom_days[insertion_index] - position - 1 == k:
                return day_with_index

            bloom_days.insert(insertion_index, position)

        return -1