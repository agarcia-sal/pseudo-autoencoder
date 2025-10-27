import heapq
from collections import defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        # Build heaps of indices for each digit character in s
        for i, c in enumerate(s):
            heapq.heappush(pos[int(c)], i)

        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            # Check if any smaller digit has an index smaller than the smallest index of the current digit
            curr_min = pos[digit][0]
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < curr_min:
                    return False
            heapq.heappop(pos[digit])
        return True