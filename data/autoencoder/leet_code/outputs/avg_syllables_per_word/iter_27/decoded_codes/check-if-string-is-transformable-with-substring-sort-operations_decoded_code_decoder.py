from collections import deque, defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)

        for index, ch in enumerate(s):
            current_digit = int(ch)
            pos[current_digit].append(index)

        for ch in t:
            current_digit = int(ch)
            if not pos[current_digit]:
                return False
            current_pos = pos[current_digit][0]
            for smaller_digit in range(current_digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < current_pos:
                    return False
            pos[current_digit].popleft()

        return True