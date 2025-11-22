from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1
        if target == "0000":
            return 0

        def neighbors(state: str) -> List[str]:
            result = []
            for i in range(4):
                digit = int(state[i])
                for move_value in (-1, 1):
                    new_digit = digit + move_value
                    if new_digit < 0:
                        new_digit += 10
                    elif new_digit >= 10:
                        new_digit -= 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    result.append(new_state)
            return result

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            current_state, steps = queue.popleft()
            for neighbor_state in neighbors(current_state):
                if neighbor_state not in visited and neighbor_state not in deadends_set:
                    if neighbor_state == target:
                        return steps + 1
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, steps + 1))

        return -1