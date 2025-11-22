from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix_sum = self.construct_prefix_sum(stoneValue)

        def get_range_sum(left: int, right: int) -> int:
            # Sum of stoneValue[left:right+1]
            return prefix_sum[right + 1] - prefix_sum[left]

        from functools import lru_cache

        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return 0
            max_score = 0
            for index in range(left, right):
                left_sum = get_range_sum(left, index)
                right_sum = get_range_sum(index + 1, right)
                if left_sum < right_sum:
                    max_score = max(max_score, left_sum + dp(left, index))
                elif left_sum > right_sum:
                    max_score = max(max_score, right_sum + dp(index + 1, right))
                else:
                    max_score = max(max_score,
                                    left_sum + dp(left, index),
                                    right_sum + dp(index + 1, right))
            return max_score

        return dp(0, len(stoneValue) - 1)

    def construct_prefix_sum(self, list_of_values: List[int]) -> List[int]:
        prefix_sum_list = [0] * (len(list_of_values) + 1)
        for i in range(len(list_of_values)):
            prefix_sum_list[i + 1] = prefix_sum_list[i] + list_of_values[i]
        return prefix_sum_list