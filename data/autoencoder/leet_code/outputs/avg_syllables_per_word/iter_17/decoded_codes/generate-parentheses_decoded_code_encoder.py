class Solution:
    def generateParenthesis(self, number_n: int) -> list[str]:
        result_list = []

        def backtrack(string_s: str = "", left_count: int = 0, right_count: int = 0) -> None:
            if len(string_s) == 2 * number_n:
                result_list.append(string_s)
                return
            if left_count < number_n:
                backtrack(string_s + "(", left_count + 1, right_count)
            if right_count < left_count:
                backtrack(string_s + ")", left_count, right_count + 1)

        backtrack()
        return result_list