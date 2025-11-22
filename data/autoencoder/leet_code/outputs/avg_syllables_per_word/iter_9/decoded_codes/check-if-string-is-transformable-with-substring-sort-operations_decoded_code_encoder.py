import heapq

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = {d: [] for d in range(10)}
        for i, c in enumerate(s):
            heapq.heappush(pos[int(c)], i)

        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            idx = pos[digit][0]
            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < idx:
                    return False
            heapq.heappop(pos[digit])
        return True