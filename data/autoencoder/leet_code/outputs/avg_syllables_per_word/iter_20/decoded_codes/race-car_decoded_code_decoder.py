from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        pointer = deque([(0, 1, 0)])  # position, speed, steps
        visited = {(0, 1)}

        while pointer:
            position, speed, steps = pointer.popleft()
            if position == target:
                return steps

            next_position = position + speed
            next_speed = speed * 2

            if 0 <= next_position < 2 * target and (next_position, next_speed) not in visited:
                visited.add((next_position, next_speed))
                pointer.append((next_position, next_speed, steps + 1))

            if speed > 0:
                next_speed = -1
            else:
                next_speed = 1

            if 0 <= position < 2 * target and (position, next_speed) not in visited:
                visited.add((position, next_speed))
                pointer.append((position, next_speed, steps + 1))