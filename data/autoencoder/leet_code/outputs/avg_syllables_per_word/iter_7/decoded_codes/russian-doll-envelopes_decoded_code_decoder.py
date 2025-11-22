from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in envelopes:
            idx = bisect.bisect_left(dp, height)
            if idx == len(dp):
                dp.append(height)
            else:
                dp[idx] = height
        return len(dp)