from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}
        limit = 2 * target

        while queue:
            position, speed, steps = queue.popleft()
            if position == target:
                return steps

            next_position = position + speed
            next_speed = speed * 2
            if 0 <= next_position < limit and (next_position, next_speed) not in visited:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            new_speed = -1 if speed > 0 else 1
            if 0 <= position < limit and (position, new_speed) not in visited:
                visited.add((position, new_speed))
                queue.append((position, new_speed, steps + 1))