from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        positions = [deque() for _ in range(10)]
        for idx, ch in enumerate(s):
            positions[int(ch)].append(idx)
        for ch in t:
            digit = int(ch)
            if not positions[digit]:
                return False
            for smaller_digit in range(digit):
                if positions[smaller_digit] and positions[smaller_digit][0] < positions[digit][0]:
                    return False
            positions[digit].popleft()
        return True