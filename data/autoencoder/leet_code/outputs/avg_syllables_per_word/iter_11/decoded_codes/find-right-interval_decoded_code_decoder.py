from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts = [start for start, _ in start_times]
        result = []
        for interval in intervals:
            idx = bisect_left(starts, interval[1])
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result