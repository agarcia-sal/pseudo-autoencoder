class Solution:
    def diffWaysToCompute(self, expression: str):
        from functools import lru_cache

        def compute(left, right, operator):
            results = []
            for l in left:
                for r in right:
                    if operator == '+':
                        results.append(l + r)
                    elif operator == '-':
                        results.append(l - r)
                    else:  # operator == '*'
                        results.append(l * r)
            return results

        @lru_cache(None)
        def helper(sub_expr):
            if sub_expr.isdigit():
                return [int(sub_expr)]

            results = []
            for i, char in enumerate(sub_expr):
                if char in "+-*":
                    left_results = helper(sub_expr[:i])
                    right_results = helper(sub_expr[i + 1:])
                    results.extend(compute(left_results, right_results, char))
            return results

        return helper(expression)