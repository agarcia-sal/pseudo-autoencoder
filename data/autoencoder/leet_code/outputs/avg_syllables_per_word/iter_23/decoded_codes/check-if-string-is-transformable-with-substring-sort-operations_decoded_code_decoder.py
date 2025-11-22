from collections import defaultdict, deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)  # digit : deque of indices in ascending order

        for index, ch in enumerate(s):
            digit = int(ch)
            pos[digit].append(index)

        for ch in t:
            digit = int(ch)
            if not pos[digit]:
                return False
            # Check all smaller digits if any has index lower than current digit's first index
            current_index = pos[digit][0]
            for smaller_digit in range(digit):
                if pos[smaller_digit] and pos[smaller_digit][0] < current_index:
                    return False
            pos[digit].popleft()

        return True