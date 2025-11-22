class Solution:
    def stoneGameV(self, stoneValue):
        prefix_sum = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue)):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

        def get_range_sum(left, right):
            return prefix_sum[right + 1] - prefix_sum[left]

        from functools import lru_cache

        @lru_cache(None)
        def dp(left, right):
            if left == right:
                return 0
            max_score = 0
            for i in range(left, right):
                left_sum = get_range_sum(left, i)
                right_sum = get_range_sum(i + 1, right)
                if left_sum < right_sum:
                    max_score = max(max_score, left_sum + dp(left, i))
                elif left_sum > right_sum:
                    max_score = max(max_score, right_sum + dp(i + 1, right))
                else:
                    max_score = max(max_score, 
                                    left_sum + dp(left, i),
                                    right_sum + dp(i + 1, right))
            return max_score

        return dp(0, len(stoneValue) - 1)