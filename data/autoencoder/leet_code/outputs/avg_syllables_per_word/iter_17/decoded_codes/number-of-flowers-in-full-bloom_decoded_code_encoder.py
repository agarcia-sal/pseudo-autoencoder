from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            count_of_flowers_in_bloom = started - ended
            result.append(count_of_flowers_in_bloom)
        return result