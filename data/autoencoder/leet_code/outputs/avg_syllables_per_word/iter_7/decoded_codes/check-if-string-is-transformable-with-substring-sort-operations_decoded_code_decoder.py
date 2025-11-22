from typing import List, Dict
import heapq
from collections import defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos: Dict[int, List[int]] = defaultdict(list)
        for i, c in enumerate(s):
            digit = int(c)
            heapq.heappush(pos[digit], i)
        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < pos[digit][0]:
                    return False
            heapq.heappop(pos[digit])
        return True