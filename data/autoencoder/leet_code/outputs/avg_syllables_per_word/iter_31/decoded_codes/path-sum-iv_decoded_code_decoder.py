from typing import List

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth: int, pos: int, path_sum: int) -> int:
            current_value = tree.get((depth, pos))
            if current_value is None:
                return 0
            new_path_sum = path_sum + current_value
            left_child_depth = depth + 1
            left_child_pos = pos * 2 - 1
            right_child_depth = depth + 1
            right_child_pos = pos * 2
            left_exists = (left_child_depth, left_child_pos) in tree
            right_exists = (right_child_depth, right_child_pos) in tree
            if not left_exists and not right_exists:
                return new_path_sum
            left_sum = dfs(left_child_depth, left_child_pos, new_path_sum)
            right_sum = dfs(right_child_depth, right_child_pos, new_path_sum)
            return left_sum + right_sum

        return dfs(1, 1, 0)