from bisect import bisect_right, bisect_left

class Solution:
    def fullBloomFlowers(self, flowers, people):
        start_times = [flower[0] for flower in flowers]
        start_times.sort()
        end_times = [flower[1] for flower in flowers]
        end_times.sort()

        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            in_bloom = started - ended
            result.append(in_bloom)

        return result