from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        if target == "0000":
            return 0

        def neighbors(state):
            result = []
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    result.append(new_state)
            return result

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            current_state, steps = queue.popleft()
            for neighbor in neighbors(current_state):
                if neighbor not in visited and neighbor not in deadends_set:
                    if neighbor == target:
                        return steps + 1
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return -1