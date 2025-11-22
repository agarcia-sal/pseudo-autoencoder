class Solution:
    def pathSum(self, list_of_numbers):
        tree = {}
        for number in list_of_numbers:
            depth = number // 100
            position = (number // 10) % 10
            value = number % 10
            tree[(depth, position)] = value

        def dfs(depth_value, position_value, path_sum_value):
            current_value = tree.get((depth_value, position_value))
            if current_value is None:
                return 0

            new_path_sum = path_sum_value + current_value

            left_child_depth = depth_value + 1
            left_child_position = position_value * 2 - 1
            right_child_depth = depth_value + 1
            right_child_position = position_value * 2

            left_child_exists = (left_child_depth, left_child_position) in tree
            right_child_exists = (right_child_depth, right_child_position) in tree

            if not left_child_exists and not right_child_exists:
                return new_path_sum

            left_sum = dfs(left_child_depth, left_child_position, new_path_sum)
            right_sum = dfs(right_child_depth, right_child_position, new_path_sum)

            return left_sum + right_sum

        return dfs(1, 1, 0)