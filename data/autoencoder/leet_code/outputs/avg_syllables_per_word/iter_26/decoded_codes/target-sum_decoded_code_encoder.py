class Solution:
    def findTargetSumWays(self, list_of_numbers, target_value):
        def dfs(current_index, current_sum_value, memo_dictionary):
            if current_index == len(list_of_numbers):
                return 1 if current_sum_value == target_value else 0
            if (current_index, current_sum_value) in memo_dictionary:
                return memo_dictionary[(current_index, current_sum_value)]

            positive_result = dfs(current_index + 1, current_sum_value + list_of_numbers[current_index], memo_dictionary)
            negative_result = dfs(current_index + 1, current_sum_value - list_of_numbers[current_index], memo_dictionary)

            memo_dictionary[(current_index, current_sum_value)] = positive_result + negative_result
            return memo_dictionary[(current_index, current_sum_value)]

        return dfs(0, 0, {})