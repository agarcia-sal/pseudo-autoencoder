from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])

        while queue:
            position, speed, steps = queue.popleft()

            if position == target:
                return steps

            next_position = position + speed
            next_speed = speed * 2
            if 0 <= next_position < 2 * target and (next_position, next_speed) not in visited:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            rev_speed = -1 if speed > 0 else 1
            if 0 <= position < 2 * target and (position, rev_speed) not in visited:
                visited.add((position, rev_speed))
                queue.append((position, rev_speed, steps + 1))