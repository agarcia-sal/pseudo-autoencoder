from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], operator: str) -> List[int]:
            results = []
            for l in left:
                for r in right:
                    if operator == '+':
                        results.append(l + r)
                    elif operator == '-':
                        results.append(l - r)
                    elif operator == '*':
                        results.append(l * r)
            return results

        def helper(sub_expr: str) -> List[int]:
            if sub_expr.isdigit():
                return [int(sub_expr)]

            results = []
            for index, char in enumerate(sub_expr):
                if char in '+-*':
                    left_results = helper(sub_expr[:index])
                    right_results = helper(sub_expr[index + 1 :])
                    results.extend(compute(left_results, right_results, char))
            return results

        return helper(expression)