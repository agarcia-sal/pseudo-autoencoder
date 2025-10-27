from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # position=0, speed=1, steps=0
        visited = set([(0, 1)])
        max_pos = 2 * target

        while queue:
            position, speed, steps = queue.popleft()
            if position == target:
                return steps

            next_position = position + speed
            next_speed = speed * 2

            if 0 <= next_position < max_pos and (next_position, next_speed) not in visited:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            reverse_speed = -1 if speed > 0 else 1
            if 0 <= position < max_pos and (position, reverse_speed) not in visited:
                visited.add((position, reverse_speed))
                queue.append((position, reverse_speed, steps + 1))