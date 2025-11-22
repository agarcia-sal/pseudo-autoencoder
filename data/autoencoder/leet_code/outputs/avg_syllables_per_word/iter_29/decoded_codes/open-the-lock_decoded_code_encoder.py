from collections import deque

class Solution:
    def openLock(self, deadends_param: list[str], target_param: str) -> int:
        deadends_set = set(deadends_param)
        start = "0000"
        if start in deadends_set:
            return -1
        if target_param == start:
            return 0

        queue = deque([(start, 0)])
        visited = {start}

        def neighbors(parameter_state: str) -> list[str]:
            result = []
            for index in range(4):
                digit = int(parameter_state[index])
                for move_value in (-1, 1):
                    new_digit = (digit + move_value) % 10
                    new_state = (
                        parameter_state[:index]
                        + str(new_digit)
                        + parameter_state[index+1:]
                    )
                    result.append(new_state)
            return result

        while queue:
            current_state, steps = queue.popleft()
            for neighbor_state in neighbors(current_state):
                if neighbor_state not in visited and neighbor_state not in deadends_set:
                    if neighbor_state == target_param:
                        return steps + 1
                    visited.add(neighbor_state)
                    queue.append((neighbor_state, steps + 1))
        return -1