from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width ascending and height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in envelopes:
            idx = bisect_left(dp, height)
            if idx == len(dp):
                dp.append(height)
            else:
                dp[idx] = height
        return len(dp)