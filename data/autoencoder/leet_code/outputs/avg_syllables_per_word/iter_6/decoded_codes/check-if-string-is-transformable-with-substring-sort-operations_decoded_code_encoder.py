from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, ch in enumerate(s):
            heappush(pos[int(ch)], i)

        for ch in t:
            digit = int(ch)
            if not pos[digit]:
                return False
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < pos[digit][0]:
                    return False
            heappop(pos[digit])

        return True