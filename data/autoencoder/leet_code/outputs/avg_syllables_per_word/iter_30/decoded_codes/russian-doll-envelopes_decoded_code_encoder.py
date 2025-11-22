from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort by width ascending and height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            idx = bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)