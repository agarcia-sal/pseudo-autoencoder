from functools import cache

class Solution:
    def stoneGameV(self, stoneValue):
        prefix_sum = self.initialize_prefix_sum(stoneValue)

        def get_range_sum(left, right):
            return prefix_sum[right + 1] - prefix_sum[left]

        @cache
        def dp(left, right):
            if left == right:
                return 0
            max_score = 0
            for i in range(left, right):
                left_sum = get_range_sum(left, i)
                right_sum = get_range_sum(i + 1, right)
                if left_sum < right_sum:
                    possible_score = left_sum + dp(left, i)
                    max_score = max(max_score, possible_score)
                elif left_sum > right_sum:
                    possible_score = right_sum + dp(i + 1, right)
                    max_score = max(max_score, possible_score)
                else:
                    option1 = left_sum + dp(left, i)
                    option2 = right_sum + dp(i + 1, right)
                    max_score = max(max_score, option1, option2)
            return max_score

        return dp(0, len(stoneValue) - 1)

    def initialize_prefix_sum(self, stoneValue):
        prefix_sum = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue)):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]
        return prefix_sum