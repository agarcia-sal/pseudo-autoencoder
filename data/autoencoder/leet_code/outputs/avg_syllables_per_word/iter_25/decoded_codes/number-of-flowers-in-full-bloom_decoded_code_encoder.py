from bisect import bisect_right, bisect_left

class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = sorted(f[0] for f in flowers)
        end_times = sorted(f[1] for f in flowers)
        result = []
        for person in people:
            # Count of flowers started blooming at or before 'person'
            started = bisect_right(start_times, person)
            # Count of flowers ended blooming before 'person'
            ended = bisect_left(end_times, person)
            result.append(started - ended)
        return result