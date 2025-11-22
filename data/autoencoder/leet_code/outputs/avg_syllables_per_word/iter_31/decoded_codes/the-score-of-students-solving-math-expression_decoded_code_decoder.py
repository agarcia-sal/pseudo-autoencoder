from typing import List, Set

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def evaluate_expression(expression: str) -> int:
            tokens = []
            num = 0
            # Tokenize the expression into numbers and operators
            for ch in expression:
                if ch.isdigit():
                    num = num * 10 + int(ch)
                else:
                    tokens.append(num)
                    tokens.append(ch)
                    num = 0
            tokens.append(num)

            # Evaluate all multiplications first (left-to-right)
            i = 1
            while i < len(tokens):
                if tokens[i] == '*':
                    tokens[i-1] = tokens[i-1] * tokens[i+1]
                    del tokens[i:i+2]  # remove operator and the right operand
                else:
                    i += 1

            # Evaluate additions (left-to-right)
            result = tokens[0]
            i = 1
            while i < len(tokens):
                if tokens[i] == '+':
                    result += tokens[i+1]
                i += 2

            return result

        def get_possible_answers(expression: str) -> Set[int]:
            if expression.isdigit():
                return {int(expression)}

            results = set()
            # Split expression at every operator position (odd indices), recursively compute results
            for i in range(1, len(expression), 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i+1:])
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