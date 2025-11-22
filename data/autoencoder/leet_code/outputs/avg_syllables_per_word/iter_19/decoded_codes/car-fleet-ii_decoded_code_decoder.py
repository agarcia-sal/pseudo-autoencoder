from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        result = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i][0], cars[i][1]

            while stack:
                next_index = stack[-1]
                next_pos, next_speed = cars[next_index][0], cars[next_index][1]

                if speed <= next_speed:
                    stack.pop()
                    continue

                collision_time = (next_pos - pos) / (speed - next_speed)

                if result[next_index] > 0 and collision_time >= result[next_index]:
                    stack.pop()
                    continue

                result[i] = collision_time
                break

            stack.append(i)

        return result