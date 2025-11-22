from typing import List, Dict, Tuple, Optional

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree: Dict[Tuple[int, int], int] = {}

        # Build tree dictionary with keys as (depth, pos) and values as node value
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth: int, pos: int, path_sum: int) -> int:
            current_value: Optional[int] = tree.get((depth, pos))
            if current_value is None:
                return 0

            new_path_sum = path_sum + current_value

            left_child = (depth + 1, pos * 2 - 1)
            right_child = (depth + 1, pos * 2)

            left_exists = left_child in tree
            right_exists = right_child in tree

            # If leaf node
            if not left_exists and not right_exists:
                return new_path_sum

            left_sum = dfs(*left_child, new_path_sum) if left_exists else 0
            right_sum = dfs(*right_child, new_path_sum) if right_exists else 0

            return left_sum + right_sum

        return dfs(1, 1, 0)