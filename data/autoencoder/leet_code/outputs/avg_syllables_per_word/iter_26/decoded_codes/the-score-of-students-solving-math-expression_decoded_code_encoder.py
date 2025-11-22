class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        def evaluate_expression(expression: str) -> int:
            tokens = []
            number_buffer = 0
            for ch in expression:
                if ch.isdigit():
                    number_buffer = number_buffer * 10 + int(ch)
                else:
                    tokens.append(number_buffer)
                    tokens.append(ch)
                    number_buffer = 0
            tokens.append(number_buffer)

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

        def get_possible_answers(expression: str) -> set[int]:
            if expression.isdigit():
                return {int(expression)}

            results = set()
            length = len(expression)
            # Operators are at odd indices in expression
            for i in range(1, length - 1, 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i + 1:])
                operator = expression[i]
                for lv in left_results:
                    for rv in right_results:
                        if operator == '+':
                            res = lv + rv
                        else:
                            res = lv * rv
                        if res <= 1000:
                            results.add(res)
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