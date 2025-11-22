from collections import deque, defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        for c in t:
            d = int(c)
            if not pos[d]:
                return False
            for smaller in range(d):
                if pos[smaller] and pos[smaller][0] < pos[d][0]:
                    return False
            pos[d].popleft()
        return True