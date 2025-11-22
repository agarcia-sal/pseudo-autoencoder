class Solution:
    def scoreOfParentheses(self, string_s: str) -> int:
        stack_list = []
        score_value = 0
        for character in string_s:
            if character == '(':
                stack_list.append(score_value)
                score_value = 0
            else:
                popped_score = stack_list.pop()
                if score_value == 0:
                    score_value = popped_score + 1
                else:
                    score_value = popped_score + 2 * score_value
        return score_value