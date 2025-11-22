from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        if target == "0000":
            return 0

        queue = deque([("0000", 0)])
        visited = {"0000"}

        def neighbors(state: str) -> List[str]:
            result = []
            for position in range(4):
                digit = int(state[position])
                for movement in (-1, 1):
                    new_digit = (digit + movement) % 10
                    new_state = state[:position] + str(new_digit) + state[position + 1:]
                    result.append(new_state)
            return result

        while queue:
            current_state, steps = queue.popleft()
            for neighbor_state in neighbors(current_state):
                if neighbor_state not in visited and neighbor_state not in deadends_set:
                    if neighbor_state == target:
                        return steps + 1
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, steps + 1))

        return -1