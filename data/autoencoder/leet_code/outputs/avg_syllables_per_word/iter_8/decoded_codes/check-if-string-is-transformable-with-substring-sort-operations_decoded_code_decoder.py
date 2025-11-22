import heapq

class Solution:
    def isTransformable(self, s, t):
        pos = {i: [] for i in range(10)}
        for i, c in enumerate(s):
            digit = int(c)
            heapq.heappush(pos[digit], i)
        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False
            for smaller_digit in range(digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < pos[digit][0]:
                    return False
            heapq.heappop(pos[digit])
        return True