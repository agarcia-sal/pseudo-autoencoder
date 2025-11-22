class Solution:
    def canSeePersonsCount(self, heights):
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] < heights[i]:
                answer[stack.pop()] += 1
            if stack:
                answer[stack[-1]] += 1
            stack.append(i)

        return answer