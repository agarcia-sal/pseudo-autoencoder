from bisect import bisect_left, insort

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        bloom_days = []
        for day, position in enumerate(bulbs, start=1):
            insertion_index = bisect_left(bloom_days, position)
            # Check left neighbor
            if insertion_index > 0 and position - bloom_days[insertion_index - 1] - 1 == k:
                return day
            # Check right neighbor
            if insertion_index < len(bloom_days) and bloom_days[insertion_index] - position - 1 == k:
                return day
            insort(bloom_days, position)
        return -1