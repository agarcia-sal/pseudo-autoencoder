class Solution:
    def pathSum(self, nums):
        tree = {}
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            value = num % 10
            if depth not in tree:
                tree[depth] = {}
            tree[depth][pos] = value

        def dfs(depth, pos, path_sum):
            if depth not in tree or pos not in tree[depth]:
                return 0

            current_value = tree[depth][pos]
            new_path_sum = path_sum + current_value

            left_child_depth = depth + 1
            left_child_pos = 2 * pos - 1
            right_child_depth = depth + 1
            right_child_pos = 2 * pos

            left_exists = left_child_depth in tree and left_child_pos in tree[left_child_depth]
            right_exists = right_child_depth in tree and right_child_pos in tree[right_child_depth]

            if not left_exists and not right_exists:
                return new_path_sum

            left_sum = dfs(left_child_depth, left_child_pos, new_path_sum)
            right_sum = dfs(right_child_depth, right_child_pos, new_path_sum)

            return left_sum + right_sum

        return dfs(1, 1, 0)