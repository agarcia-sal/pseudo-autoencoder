from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort by width ascending and height descending when widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in envelopes:
            index = bisect_left(dp, height)
            if index == len(dp):
                dp.append(height)
            else:
                dp[index] = height
        return len(dp)