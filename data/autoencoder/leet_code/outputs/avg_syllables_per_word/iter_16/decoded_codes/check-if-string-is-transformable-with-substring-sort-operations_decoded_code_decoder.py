from collections import defaultdict, deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)
        for i, c in enumerate(s):
            pos[int(c)].append(i)

        for c in t:
            digit = int(c)
            if not pos[digit]:
                return False
            for smaller_digit in range(digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < pos[digit][0]:
                    return False
            pos[digit].popleft()

        return True