from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for p in people:
            started = bisect_right(start_times, p)  # number of flowers started blooming at or before p
            ended = bisect_left(end_times, p)       # number of flowers ended blooming before p
            result.append(started - ended)
        return result