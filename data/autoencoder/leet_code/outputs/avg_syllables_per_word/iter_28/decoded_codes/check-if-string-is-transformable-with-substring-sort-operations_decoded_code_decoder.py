from collections import defaultdict
import heapq

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        position_map = defaultdict(list)
        for i, c in enumerate(s):
            digit_value = int(c)
            heapq.heappush(position_map[digit_value], i)

        for i, c in enumerate(t):
            current_digit = int(c)
            if not position_map[current_digit]:
                return False
            for smaller_digit in range(current_digit):
                if position_map[smaller_digit] and position_map[smaller_digit][0] < position_map[current_digit][0]:
                    return False
            heapq.heappop(position_map[current_digit])

        return True