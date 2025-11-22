from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = sorted(s for s, e in flowers)
        end_times = sorted(e for s, e in flowers)
        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            result.append(started - ended)
        return result