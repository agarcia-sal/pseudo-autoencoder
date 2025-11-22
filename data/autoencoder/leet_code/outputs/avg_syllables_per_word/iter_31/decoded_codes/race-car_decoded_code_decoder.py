from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # position, speed, steps
        visited = set([(0, 1)])

        while queue:
            position, speed, steps = queue.popleft()

            if position == target:
                return steps

            # Move forward
            next_position = position + speed
            next_speed = speed * 2
            if (next_position, next_speed) not in visited and 0 <= next_position < 2 * target:
                visited.add((next_position, next_speed))
                queue.append((next_position, next_speed, steps + 1))

            # Reverse
            if speed > 0:
                rev_speed = -1
            else:
                rev_speed = 1

            if (position, rev_speed) not in visited and 0 <= position < 2 * target:
                visited.add((position, rev_speed))
                queue.append((position, rev_speed, steps + 1))