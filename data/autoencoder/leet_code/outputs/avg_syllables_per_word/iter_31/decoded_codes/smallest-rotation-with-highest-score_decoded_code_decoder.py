from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        delta = [0] * n

        for i, num in enumerate(nums):
            if num <= i:
                delta[0] += 1
                end = i - num + 1
                if end < n:
                    delta[end] -= 1
            if i + 1 < n:
                delta[i + 1] += 1
                end = i + n - num + 1
                if end < n:
                    delta[end] -= 1

        score = 0
        max_score = 0
        best_k = 0

        for k in range(n):
            score += delta[k]
            if score > max_score:
                max_score = score
                best_k = k

        return best_k