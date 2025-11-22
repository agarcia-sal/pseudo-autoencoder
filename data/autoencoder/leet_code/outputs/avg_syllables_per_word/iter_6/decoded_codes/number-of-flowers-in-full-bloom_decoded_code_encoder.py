from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for p in people:
            started = bisect_right(start_times, p)
            ended = bisect_left(end_times, p)
            result.append(started - ended)
        return result