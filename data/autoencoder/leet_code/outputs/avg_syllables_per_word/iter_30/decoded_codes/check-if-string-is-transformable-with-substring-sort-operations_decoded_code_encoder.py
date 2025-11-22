from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = {str(d): deque() for d in range(10)}
        # Store indices of each digit in s
        for i, c in enumerate(s):
            pos[c].append(i)
        for c in t:
            digit = c
            if not pos[digit]:
                return False
            for smaller in map(str, range(int(digit))):
                if pos[smaller] and pos[smaller][0] < pos[digit][0]:
                    return False
            pos[digit].popleft()
        return True