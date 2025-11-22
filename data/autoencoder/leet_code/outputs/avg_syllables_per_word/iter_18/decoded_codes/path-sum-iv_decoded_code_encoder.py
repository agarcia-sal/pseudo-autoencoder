from collections import defaultdict

class Solution:
    def pathSum(self, nums):
        tree = {}
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth, pos, path_sum):
            current_value = tree.get((depth, pos))
            if current_value is None:
                return 0
            new_path_sum = path_sum + current_value
            left_child = (depth + 1, pos * 2 - 1)
            right_child = (depth + 1, pos * 2)
            if left_child not in tree and right_child not in tree:
                return new_path_sum
            left_sum = dfs(left_child[0], left_child[1], new_path_sum)
            right_sum = dfs(right_child[0], right_child[1], new_path_sum)
            return left_sum + right_sum

        return dfs(1, 1, 0)