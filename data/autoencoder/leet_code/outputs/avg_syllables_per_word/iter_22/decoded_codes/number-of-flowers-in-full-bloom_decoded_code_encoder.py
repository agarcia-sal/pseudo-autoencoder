from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for person in people:
            # bisect_right for start_times to count flowers started at or before person
            number_of_started_flowers = bisect_right(start_times, person)
            # bisect_left for end_times to count flowers ended strictly before person
            number_of_ended_flowers = bisect_left(end_times, person)
            number_of_flowers_in_bloom = number_of_started_flowers - number_of_ended_flowers
            result.append(number_of_flowers_in_bloom)
        return result