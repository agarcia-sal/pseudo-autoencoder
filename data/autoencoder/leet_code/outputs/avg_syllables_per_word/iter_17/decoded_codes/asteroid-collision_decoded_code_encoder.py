class Solution:
    def asteroidCollision(self, list_of_asteroids):
        stack = []
        for asteroid in list_of_asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack