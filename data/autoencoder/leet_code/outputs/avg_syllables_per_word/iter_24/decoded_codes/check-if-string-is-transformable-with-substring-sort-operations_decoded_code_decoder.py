import heapq

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = {digit: [] for digit in range(10)}
        for i, c in enumerate(s):
            digit = int(c)
            heapq.heappush(pos[digit], i)
        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False
            curr_index = pos[digit][0]
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < curr_index:
                    return False
            heapq.heappop(pos[digit])
        return True