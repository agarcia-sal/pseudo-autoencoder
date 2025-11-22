from collections import defaultdict

class Solution:
    def pathSum(self, nums):
        tree = defaultdict(dict)
        for num in nums:
            depth = num // 100
            pos = (num % 100) // 10
            value = num % 10
            tree[depth][pos] = value

        def dfs(depth, pos, path_sum):
            current_value = tree.get(depth, {}).get(pos)
            if current_value is None:
                return 0
            new_path_sum = path_sum + current_value
            left_child_depth = depth + 1
            left_child_pos = pos * 2 - 1
            right_child_depth = depth + 1
            right_child_pos = pos * 2
            left_exists = left_child_pos in tree.get(left_child_depth, {})
            right_exists = right_child_pos in tree.get(right_child_depth, {})
            if not left_exists and not right_exists:
                return new_path_sum
            left_sum = dfs(left_child_depth, left_child_pos, new_path_sum)
            right_sum = dfs(right_child_depth, right_child_pos, new_path_sum)
            return left_sum + right_sum

        return dfs(1, 1, 0)