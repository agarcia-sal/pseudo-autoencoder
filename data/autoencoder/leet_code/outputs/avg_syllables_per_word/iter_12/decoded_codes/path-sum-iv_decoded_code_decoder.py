from collections import defaultdict

class Solution:
    def pathSum(self, nums):
        tree = defaultdict(lambda: None)
        for num in nums:
            depth = num // 100
            pos = (num % 100) // 10
            value = num % 10
            tree[(depth, pos)] = value

        def dfs(depth, pos, path_sum):
            current_value = tree[(depth, pos)]
            if current_value is None:
                return 0

            new_path_sum = path_sum + current_value
            left_child = (depth + 1, pos * 2 - 1)
            right_child = (depth + 1, pos * 2)

            if tree[left_child] is None and tree[right_child] is None:
                return new_path_sum

            left_sum = dfs(depth + 1, pos * 2 - 1, new_path_sum)
            right_sum = dfs(depth + 1, pos * 2, new_path_sum)

            return left_sum + right_sum

        return dfs(1, 1, 0)