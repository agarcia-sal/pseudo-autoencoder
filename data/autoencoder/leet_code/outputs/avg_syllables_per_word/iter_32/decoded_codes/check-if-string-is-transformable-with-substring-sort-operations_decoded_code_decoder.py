import heapq
from collections import defaultdict
from typing import List

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # Map digits 0-9 to min-heaps of indices where they appear in s
        pos = defaultdict(list)
        for index, char in enumerate(s):
            digit = int(char)
            heapq.heappush(pos[digit], index)

        for char in t:
            digit = int(char)
            if not pos[digit]:
                # digit does not appear in s or no indices left
                return False

            # smallest index of current digit in s
            digit_pos = pos[digit][0]

            # Check for smaller digits that appear before digit_pos
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < digit_pos:
                    return False

            # Use the smallest index for digit from pos
            heapq.heappop(pos[digit])

        return True