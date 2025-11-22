import bisect

class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for p in people:
            started = bisect.bisect_right(start_times, p)  # count of flowers started blooming by time p
            ended = bisect.bisect_left(end_times, p)       # count of flowers ended blooming before time p
            result.append(started - ended)
        return result