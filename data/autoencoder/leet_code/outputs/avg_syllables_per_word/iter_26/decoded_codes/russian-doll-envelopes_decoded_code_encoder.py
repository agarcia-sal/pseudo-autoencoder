from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width ascending and height descending if widths are equal
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []
        for _, height in envelopes:
            # Find the index to insert height to maintain sorted dp
            index = bisect_left(dp, height)
            if index == len(dp):
                dp.append(height)
            else:
                dp[index] = height
        return len(dp)