class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        def evaluate_expression(expression: str) -> int:
            tokens = []
            number = 0
            for char in expression:
                if char.isdigit():
                    number = number * 10 + int(char)
                else:
                    tokens.append(number)
                    tokens.append(char)
                    number = 0
            tokens.append(number)

            # Process '*' first
            index = 1
            while index < len(tokens):
                if tokens[index] == '*':
                    tokens[index - 1] = tokens[index - 1] * tokens[index + 1]
                    del tokens[index:index + 2]
                else:
                    index += 1

            # Process '+' second
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
            for i in range(1, len(expression) - 1, 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i + 1:])
                op = expression[i]
                for left in left_results:
                    for right in right_results:
                        if op == '+':
                            res = left + right
                        else:  # op == '*'
                            res = left * right
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