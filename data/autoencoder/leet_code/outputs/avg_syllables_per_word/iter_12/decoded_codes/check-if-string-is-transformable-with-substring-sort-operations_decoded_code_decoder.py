from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = {str(d): deque() for d in range(10)}
        for i, c in enumerate(s):
            pos[c].append(i)

        for c in t:
            digit = c
            if not pos[digit]:
                return False
            for smaller in range(int(digit)):
                if pos[str(smaller)] and pos[str(smaller)][0] < pos[digit][0]:
                    return False
            pos[digit].popleft()
        return True