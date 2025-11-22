from collections import deque, defaultdict

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)
        for i, c in enumerate(s):
            pos[int(c)].append(i)

        for c in t:
            digit_value = int(c)
            if not pos[digit_value]:
                return False
            current_index = pos[digit_value][0]
            for smaller_digit in range(digit_value):
                if pos[smaller_digit] and pos[smaller_digit][0] < current_index:
                    return False
            pos[digit_value].popleft()

        return True