from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for index in range(n):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = index - previous_index
            stack.append(index)

        return answer