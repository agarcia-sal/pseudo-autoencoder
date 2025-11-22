from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            result.append(started - ended)
        return result