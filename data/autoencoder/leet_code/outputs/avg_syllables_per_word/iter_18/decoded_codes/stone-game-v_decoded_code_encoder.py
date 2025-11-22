from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix_sum = [0] * (len(stoneValue) + 1)
        self.initialize_prefix_sum(stoneValue, prefix_sum)

        from functools import lru_cache

        def get_range_sum(left: int, right: int) -> int:
            return prefix_sum[right + 1] - prefix_sum[left]

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
                    max_score = max(max_score, left_sum + dp(left, index), right_sum + dp(index + 1, right))
            return max_score

        return dp(0, len(stoneValue) - 1)

    def initialize_prefix_sum(self, stone_list: List[int], prefix_list: List[int]) -> None:
        for pos in range(len(stone_list)):
            prefix_list[pos + 1] = prefix_list[pos] + stone_list[pos]