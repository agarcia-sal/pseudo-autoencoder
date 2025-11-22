from functools import lru_cache
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix_sum = [0] * (len(stoneValue) + 1)
        for index in range(len(stoneValue)):
            prefix_sum[index + 1] = prefix_sum[index] + stoneValue[index]

        def get_range_sum(left: int, right: int) -> int:
            return prefix_sum[right + 1] - prefix_sum[left]

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return 0
            max_score = 0
            for i in range(left, right):
                left_sum = get_range_sum(left, i)
                right_sum = get_range_sum(i + 1, right)
                if left_sum < right_sum:
                    candidate_score = left_sum + dp(left, i)
                    if candidate_score > max_score:
                        max_score = candidate_score
                elif left_sum > right_sum:
                    candidate_score = right_sum + dp(i + 1, right)
                    if candidate_score > max_score:
                        max_score = candidate_score
                else:
                    candidate_score_one = left_sum + dp(left, i)
                    candidate_score_two = right_sum + dp(i + 1, right)
                    if candidate_score_one > max_score:
                        max_score = candidate_score_one
                    if candidate_score_two > max_score:
                        max_score = candidate_score_two
            return max_score

        return dp(0, len(stoneValue) - 1)