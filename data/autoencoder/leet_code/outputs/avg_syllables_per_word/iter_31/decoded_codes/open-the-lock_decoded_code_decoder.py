from collections import deque
from typing import List, Set


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set: Set[str] = set(deadends)
        start = "0000"
        if start in deadends_set:
            return -1
        if target == start:
            return 0

        def neighbors(state: str) -> List[str]:
            result = []
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = digit + move
                    if new_digit < 0:
                        new_digit += 10
                    elif new_digit >= 10:
                        new_digit -= 10
                    new_state = state[:i] + str(new_digit) + state[i + 1:]
                    result.append(new_state)
            return result

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            current_state, steps = queue.popleft()
            for neighbor in neighbors(current_state):
                if neighbor not in visited and neighbor not in deadends_set:
                    if neighbor == target:
                        return steps + 1
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1