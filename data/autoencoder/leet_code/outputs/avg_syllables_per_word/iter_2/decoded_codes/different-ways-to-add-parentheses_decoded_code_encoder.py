class Solution:
    def diffWaysToCompute(self, expression: str):
        def compute(left, right, operator):
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

        def helper(sub_expr):
            if sub_expr.isdigit():
                return [int(sub_expr)]

            results = []
            for i in range(len(sub_expr)):
                if sub_expr[i] in "+-*":
                    left_results = helper(sub_expr[:i])
                    right_results = helper(sub_expr[i+1:])
                    results.extend(compute(left_results, right_results, sub_expr[i]))
            return results

        return helper(expression)