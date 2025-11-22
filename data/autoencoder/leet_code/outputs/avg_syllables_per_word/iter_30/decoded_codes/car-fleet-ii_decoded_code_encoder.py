from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[float]]) -> List[float]:
        n = len(cars)
        result = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]

            while stack:
                next_index = stack[-1]
                next_pos, next_speed = cars[next_index]

                if speed <= next_speed:
                    stack.pop()
                    continue

                collision_time = (next_pos - pos) / (speed - next_speed)

                if 0 < result[next_index] <= collision_time:
                    stack.pop()
                    continue

                result[i] = collision_time
                break

            stack.append(i)

        return result