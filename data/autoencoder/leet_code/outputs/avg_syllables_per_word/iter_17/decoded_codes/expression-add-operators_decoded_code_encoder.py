class Solution:
    def addOperators(self, num_string: str, target_integer: int):
        def dfs(current_index, current_path, current_value, previous_value):
            if current_index == len(num_string):
                if current_value == target_integer:
                    result_list.append(current_path)
                return

            for i in range(current_index + 1, len(num_string) + 1):
                operand_substring = num_string[current_index:i]
                if len(operand_substring) > 1 and operand_substring[0] == '0':
                    continue
                operand_value = int(operand_substring)

                if current_index == 0:
                    dfs(i, operand_substring, operand_value, operand_value)
                else:
                    dfs(i, current_path + '+' + operand_substring, current_value + operand_value, operand_value)
                    dfs(i, current_path + '-' + operand_substring, current_value - operand_value, -operand_value)
                    dfs(i, current_path + '*' + operand_substring,
                        current_value - previous_value + previous_value * operand_value,
                        previous_value * operand_value)

        result_list = []
        dfs(0, '', 0, 0)
        return result_list