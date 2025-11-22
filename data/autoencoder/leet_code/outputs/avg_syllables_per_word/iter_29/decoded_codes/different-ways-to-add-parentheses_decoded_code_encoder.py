class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def compute(left: list[int], right: list[int], operator: str) -> list[int]:
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

        def helper(sub_expr: str) -> list[int]:
            if sub_expr.isdigit():
                return [int(sub_expr)]

            results = []
            for idx, char in enumerate(sub_expr):
                if char in "+-*":
                    left_results = helper(sub_expr[:idx])
                    right_results = helper(sub_expr[idx + 1:])
                    results.extend(compute(left_results, right_results, char))
            return results

        return helper(expression)