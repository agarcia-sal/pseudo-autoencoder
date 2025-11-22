from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = [flower[0] for flower in flowers]
        end_times = [flower[1] for flower in flowers]
        start_times.sort()
        end_times.sort()

        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            flowers_in_bloom = started - ended
            result.append(flowers_in_bloom)

        return result