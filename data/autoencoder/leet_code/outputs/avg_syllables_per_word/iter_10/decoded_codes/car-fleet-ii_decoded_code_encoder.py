class Solution:
    def getCollisionTimes(self, cars):
        n = len(cars)
        result = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]

            while stack:
                next_i = stack[-1]
                next_pos, next_speed = cars[next_i]

                if speed <= next_speed:
                    stack.pop()
                    continue

                collision_time = (next_pos - pos) / (speed - next_speed)

                if result[next_i] > 0 and collision_time >= result[next_i]:
                    stack.pop()
                    continue

                result[i] = collision_time
                break

            stack.append(i)

        return result