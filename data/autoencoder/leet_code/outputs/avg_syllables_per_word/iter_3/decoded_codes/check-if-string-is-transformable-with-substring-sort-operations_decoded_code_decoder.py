from collections import defaultdict
import heapq

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            heapq.heappush(pos[int(c)], i)
        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < pos[digit][0]:
                    return False
            heapq.heappop(pos[digit])
        return True