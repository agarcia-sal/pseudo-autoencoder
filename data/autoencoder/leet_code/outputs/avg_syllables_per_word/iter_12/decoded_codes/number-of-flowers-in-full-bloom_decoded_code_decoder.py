import bisect

class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for person in people:
            started = bisect.bisect_right(start_times, person)
            ended = bisect.bisect_left(end_times, person)
            result.append(started - ended)
        return result