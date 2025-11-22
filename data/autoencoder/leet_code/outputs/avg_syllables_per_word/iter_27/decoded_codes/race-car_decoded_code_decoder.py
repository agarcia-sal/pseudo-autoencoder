from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # (position, speed, steps)
        visited = {(0, 1)}

        while queue:
            position, speed, steps = queue.popleft()
            if position == target:
                return steps

            next_position = position + speed
            next_speed = speed * 2
            if (next_position, next_speed) not in visited and 0 <= next_position < 2 * target:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            reverse_speed = -1 if speed > 0 else 1
            if (position, reverse_speed) not in visited and 0 <= position < 2 * target:
                visited.add((position, reverse_speed))
                queue.append((position, reverse_speed, steps + 1))