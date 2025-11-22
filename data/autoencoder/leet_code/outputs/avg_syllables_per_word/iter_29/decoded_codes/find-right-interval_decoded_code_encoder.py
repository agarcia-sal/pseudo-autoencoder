from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        # Pair each interval's start time with its original index
        list_of_start_time_and_index = [(interval[0], i) for i, interval in enumerate(intervals)]
        # Sort by start time
        list_of_start_time_and_index.sort(key=lambda x: x[0])

        list_of_results = []
        starts = [pair[0] for pair in list_of_start_time_and_index]  # extract just the start times for binary search

        for interval in intervals:
            current_end_time = interval[1]
            # Find the leftmost start time >= current_end_time
            position = bisect_left(starts, current_end_time)
            if position < len(list_of_start_time_and_index):
                list_of_results.append(list_of_start_time_and_index[position][1])
            else:
                list_of_results.append(-1)

        return list_of_results