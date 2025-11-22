from typing import List, Dict, Tuple

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree: Dict[Tuple[int, int], int] = {}
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth: int, pos: int, path_sum: int) -> int:
            if (depth, pos) not in tree:
                return 0
            current_value = tree[(depth, pos)]
            new_path_sum = path_sum + current_value
            left_child = (depth + 1, pos * 2 - 1)
            right_child = (depth + 1, pos * 2)
            left_exists = left_child in tree
            right_exists = right_child in tree
            if not left_exists and not right_exists:
                return new_path_sum
            left_sum = dfs(*left_child, new_path_sum) if left_exists else 0
            right_sum = dfs(*right_child, new_path_sum) if right_exists else 0
            return left_sum + right_sum

        return dfs(1, 1, 0)