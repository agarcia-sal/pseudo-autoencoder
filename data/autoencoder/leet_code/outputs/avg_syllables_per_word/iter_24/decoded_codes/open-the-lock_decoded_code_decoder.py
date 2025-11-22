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
            for neigh in neighbors(current_state):
                if neigh not in visited and neigh not in deadends_set:
                    if neigh == target:
                        return steps + 1
                    visited.add(neigh)
                    queue.append((neigh, steps + 1))
        return -1