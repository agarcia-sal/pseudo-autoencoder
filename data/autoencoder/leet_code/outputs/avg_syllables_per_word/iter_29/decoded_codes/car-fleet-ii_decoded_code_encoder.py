from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        collision_times = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos_i, speed_i = cars[i]

            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]

                if speed_i <= speed_j:
                    stack.pop()
                    continue

                time_to_collision = (pos_j - pos_i) / (speed_i - speed_j)

                if collision_times[j] > 0 and time_to_collision >= collision_times[j]:
                    stack.pop()
                    continue

                collision_times[i] = time_to_collision
                break

            stack.append(i)

        return collision_times