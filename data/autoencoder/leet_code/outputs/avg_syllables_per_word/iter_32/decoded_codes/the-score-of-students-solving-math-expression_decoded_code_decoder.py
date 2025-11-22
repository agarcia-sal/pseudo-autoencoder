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

            i = 1
            # Process multiplication first (left to right)
            while i < len(tokens):
                if tokens[i] == '*':
                    tokens[i - 1] = tokens[i - 1] * tokens[i + 1]
                    del tokens[i:i+2]  # remove operator and right operand
                else:
                    i += 1

            result = tokens[0]
            i = 1
            # Process additions
            while i < len(tokens):
                if tokens[i] == '+':
                    result += tokens[i + 1]
                i += 2
            return result

        def get_possible_answers(expression: str) -> Set[int]:
            if expression.isdigit():
                return {int(expression)}

            results = set()
            # Operators occur at odd indices: expression[1], expression[3], ...
            for i in range(1, len(expression) - 1, 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i + 1 :])
                op = expression[i]
                for left in left_results:
                    for right in right_results:
                        if op == '+':
                            val = left + right
                        else:  # '*'
                            val = left * right
                        if val <= 1000:
                            results.add(val)
            return results

        correct_answer = evaluate_expression(s)
        possible_answers = get_possible_answers(s)

        points = 0
        for answer in answers:
            if answer == correct_answer:
                points += 5
            elif answer in possible_answers:
                points += 2

        return points