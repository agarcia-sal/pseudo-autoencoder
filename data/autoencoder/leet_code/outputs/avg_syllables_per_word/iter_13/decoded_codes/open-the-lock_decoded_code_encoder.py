from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends_set = set(deadends)
        start = "0000"

        if start in deadends_set:
            return -1
        if target == start:
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

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            current_state, steps = queue.popleft()

            for nei in neighbors(current_state):
                if nei not in visited and nei not in deadends_set:
                    if nei == target:
                        return steps + 1
                    visited.add(nei)
                    queue.append((nei, steps + 1))

        return -1