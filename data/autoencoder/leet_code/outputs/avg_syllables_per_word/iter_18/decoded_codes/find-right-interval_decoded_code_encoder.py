from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = []
        for _, end in intervals:
            idx = bisect_left(start_times, (end,))
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)
        return result