from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            digit_value = int(c)
            heappush(pos[digit_value], i)

        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False
            for smaller_digit in range(digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < pos[digit][0]:
                    return False
            heappop(pos[digit])

        return True