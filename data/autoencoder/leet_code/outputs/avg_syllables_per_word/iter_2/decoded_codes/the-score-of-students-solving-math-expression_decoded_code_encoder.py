class Solution:
    def scoreOfStudents(self, s, answers):
        def evaluate_expression(expression):
            tokens = []
            num = 0
            for char in expression:
                if char.isdigit():
                    num = num * 10 + int(char)
                else:
                    tokens.append(num)
                    tokens.append(char)
                    num = 0
            tokens.append(num)

            i = 1
            while i < len(tokens):
                if tokens[i] == '*':
                    tokens[i-1] = tokens[i-1] * tokens[i+1]
                    del tokens[i:i+2]
                else:
                    i += 1

            result = tokens[0]
            i = 1
            while i < len(tokens):
                if tokens[i] == '+':
                    result += tokens[i+1]
                i += 2

            return result

        def get_possible_answers(expression):
            if expression.isdigit():
                return {int(expression)}

            results = set()
            for i in range(1, len(expression), 2):
                left_results = get_possible_answers(expression[:i])
                right_results = get_possible_answers(expression[i+1:])
                for left in left_results:
                    for right in right_results:
                        if expression[i] == '+':
                            result = left + right
                        else:
                            result = left * right
                        if result <= 1000:
                            results.add(result)
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