from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def isTransformable(self, s, t):
        pos = defaultdict(list)

        for i, c in enumerate(s):
            heappush(pos[int(c)], i)

        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False

            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < pos[digit][0]:
                    return False

            heappop(pos[digit])

        return True