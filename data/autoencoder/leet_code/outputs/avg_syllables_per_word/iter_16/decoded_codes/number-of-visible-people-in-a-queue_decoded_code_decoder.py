from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []

        for index in range(n):
            while stack and heights[stack[-1]] < heights[index]:
                answer[stack.pop()] += 1
            if stack:
                answer[stack[-1]] += 1
            stack.append(index)

        return answer