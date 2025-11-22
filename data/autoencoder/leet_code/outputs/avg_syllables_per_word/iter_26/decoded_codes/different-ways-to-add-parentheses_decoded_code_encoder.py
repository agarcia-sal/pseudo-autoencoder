class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def compute(left_list, right_list, operator_symbol):
            results = []
            for left_element in left_list:
                for right_element in right_list:
                    if operator_symbol == '+':
                        results.append(left_element + right_element)
                    elif operator_symbol == '-':
                        results.append(left_element - right_element)
                    elif operator_symbol == '*':
                        results.append(left_element * right_element)
            return results

        def helper(sub_expression):
            if sub_expression.isdigit():
                return [int(sub_expression)]

            results = []
            for index in range(len(sub_expression)):
                if sub_expression[index] in '+-*':
                    left_results = helper(sub_expression[:index])
                    right_results = helper(sub_expression[index + 1:])
                    results.extend(compute(left_results, right_results, sub_expression[index]))
            return results

        return helper(expression)