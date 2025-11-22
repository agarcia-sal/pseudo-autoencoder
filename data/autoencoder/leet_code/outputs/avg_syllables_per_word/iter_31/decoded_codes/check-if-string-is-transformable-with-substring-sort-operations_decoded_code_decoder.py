from collections import deque
from typing import Dict, List

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos: Dict[int, deque[int]] = {d: deque() for d in range(10)}

        for i, c in enumerate(s):
            digit = int(c)
            pos[digit].append(i)

        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            curr_pos = pos[digit][0]

            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < curr_pos:
                    return False

            pos[digit].popleft()

        return True