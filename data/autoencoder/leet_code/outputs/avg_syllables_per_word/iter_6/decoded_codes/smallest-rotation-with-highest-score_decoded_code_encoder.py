class Solution:
    def bestRotation(self, nums):
        n = len(nums)
        delta = [0] * n

        for i, num in enumerate(nums):
            if num <= i:
                delta[0] += 1
                if i - num + 1 < n:
                    delta[i - num + 1] -= 1
            if i + 1 < n:
                delta[i + 1] += 1
                idx = (i + n - num) + 1
                if idx < n:
                    delta[idx] -= 1

        score = max_score = best_k = 0
        for k in range(n):
            score += delta[k]
            if score > max_score:
                max_score = score
                best_k = k

        return best_k