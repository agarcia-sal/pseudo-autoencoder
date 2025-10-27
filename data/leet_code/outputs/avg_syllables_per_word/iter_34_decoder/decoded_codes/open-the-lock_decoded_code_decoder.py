from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends_set = set(deadends)
        start = "0000"
        if start in deadends_set:
            return -1
        if target == start:
            return 0

        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        def neighbors(state):
            result = []
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = digit + move
                    if new_digit < 0:
                        new_digit = 9
                    elif new_digit > 9:
                        new_digit = 0
                    new_state = state[:i] + str(new_digit) + state[i+1:]
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