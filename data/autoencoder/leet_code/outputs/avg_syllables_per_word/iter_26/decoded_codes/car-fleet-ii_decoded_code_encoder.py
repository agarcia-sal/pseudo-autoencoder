class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        collision_times = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            while stack:
                j = stack[-1]
                next_position, next_speed = cars[j]

                if speed <= next_speed:
                    stack.pop()
                    continue

                collision_time = (next_position - position) / (speed - next_speed)

                if collision_times[j] > 0 and collision_time >= collision_times[j]:
                    stack.pop()
                    continue

                collision_times[i] = collision_time
                break

            stack.append(i)

        return collision_times