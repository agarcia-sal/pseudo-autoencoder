import bisect
from typing import List

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        bloom_days = []
        for day in range(1, len(bulbs) + 1):
            position = bulbs[day - 1]
            i = bisect.bisect_left(bloom_days, position)
            if i > 0 and position - bloom_days[i - 1] - 1 == k:
                return day
            if i < len(bloom_days) and bloom_days[i] - position - 1 == k:
                return day
            bloom_days.insert(i, position)
        return -1