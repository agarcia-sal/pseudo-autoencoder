from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        # Prepare a list of pairs (start_time, original_index), sorted by start_time
        start_times = sorted((interval[0], i) for i, interval in enumerate(intervals))

        result = []
        starts = [pair[0] for pair in start_times]  # extract start times for binary search

        for interval in intervals:
            end_value = interval[1]
            # Find the lowest start_time >= end_value
            idx = bisect_left(starts, end_value)
            if idx < len(start_times):
                result.append(start_times[idx][1])
            else:
                result.append(-1)

        return result