import heapq
from collections import defaultdict

class Solution:
    def isTransformable(self, s, t) -> bool:
        pos = defaultdict(list)
        # Build min-heaps for positions of each digit in s
        for i, c in enumerate(s):
            digit = int(c)
            heapq.heappush(pos[digit], i)
        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            # Check for any smaller digit that has a smaller index than the current digit's smallest index
            cur_idx = pos[digit][0]
            for smaller_digit in range(digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < cur_idx:
                    return False
            heapq.heappop(pos[digit])
        return True