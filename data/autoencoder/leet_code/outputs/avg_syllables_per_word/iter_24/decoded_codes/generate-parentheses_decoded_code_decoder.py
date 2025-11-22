class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(current_string="", left_count=0, right_count=0):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            if left_count < n:
                backtrack(current_string + "(", left_count + 1, right_count)
            if right_count < left_count:
                backtrack(current_string + ")", left_count, right_count + 1)

        backtrack()
        return result