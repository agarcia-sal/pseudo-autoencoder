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
            smallest_index = pos[digit][0]
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < smallest_index:
                    return False
            heapq.heappop(pos[digit])
        return True