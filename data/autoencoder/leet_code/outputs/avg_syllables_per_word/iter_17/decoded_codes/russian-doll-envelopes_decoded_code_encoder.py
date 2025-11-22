from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        list_of_heights = []
        for _, height in envelopes:
            pos = bisect_left(list_of_heights, height)
            if pos == len(list_of_heights):
                list_of_heights.append(height)
            else:
                list_of_heights[pos] = height
        return len(list_of_heights)