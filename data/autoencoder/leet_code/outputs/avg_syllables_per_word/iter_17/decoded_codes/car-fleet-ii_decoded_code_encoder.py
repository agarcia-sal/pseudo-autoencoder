from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        collision_times = [-1.0] * n
        index_stack = []

        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            while index_stack:
                next_index = index_stack[-1]
                next_position, next_speed = cars[next_index]

                if speed <= next_speed:
                    index_stack.pop()
                    continue

                collision_time = (next_position - position) / (speed - next_speed)

                if collision_times[next_index] > 0 and collision_time >= collision_times[next_index]:
                    index_stack.pop()
                    continue

                collision_times[i] = collision_time
                break

            index_stack.append(i)

        return collision_times