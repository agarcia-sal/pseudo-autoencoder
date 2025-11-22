from typing import List, Set

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def evaluate_expression(expression: str) -> int:
            tokens = []
            num = 0
            for ch in expression:
                if ch.isdigit():
                    num = num * 10 + int(ch)
                else:
                    tokens.append(num)
                    tokens.append(ch)
                    num = 0
            tokens.append(num)

            index = 1
            while index < len(tokens):
                if tokens[index] == '*':
                    tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
                    del tokens[index:index + 2]
                else:
                    index += 1

            result = tokens[0]
            index = 1
            while index < len(tokens):
                if tokens[index] == '+':
                    result += tokens[index + 1]
                index += 2
            return result

        def get_possible_answers(expression: str) -> Set[int]:
            if expression.isdigit():
                return {int(expression)}

            results = set()
            for i in range(1, len(expression) - 1, 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i + 1:])
                op = expression[i]
                for left in left_results:
                    for right in right_results:
                        if op == '+':
                            res = left + right
                        else:
                            res = left * right
                        if res <= 1000:
                            results.add(res)
            return results

        correct_answer = evaluate_expression(s)
        possible_answers = get_possible_answers(s)

        points = 0
        for ans in answers:
            if ans == correct_answer:
                points += 5
            elif ans in possible_answers:
                points += 2

        return points