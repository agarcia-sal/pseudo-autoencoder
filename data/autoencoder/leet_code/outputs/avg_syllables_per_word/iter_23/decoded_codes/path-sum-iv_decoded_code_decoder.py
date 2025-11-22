from typing import List, Dict, Tuple, Optional

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree: Dict[Tuple[int, int], int] = {}
        for num in nums:
            depth = num // 100
            pos = (num // 10) - (depth * 10)
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth: int, pos: int, path_sum: int) -> int:
            current_value: Optional[int] = tree.get((depth, pos))
            if current_value is None:
                return 0
            new_path_sum = path_sum + current_value

            left_child_depth = depth + 1
            left_child_pos = pos * 2 - 1
            right_child_depth = depth + 1
            right_child_pos = pos * 2

            left_child_key = (left_child_depth, left_child_pos)
            right_child_key = (right_child_depth, right_child_pos)

            if left_child_key not in tree and right_child_key not in tree:
                return new_path_sum

            left_sum = dfs(left_child_depth, left_child_pos, new_path_sum)
            right_sum = dfs(right_child_depth, right_child_pos, new_path_sum)

            return left_sum + right_sum

        return dfs(1, 1, 0)