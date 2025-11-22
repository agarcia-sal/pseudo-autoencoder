class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side: str):
            # Insert separators before '+' and '-' to split tokens correctly,
            # taking care of the first character if it's '+' or '-'
            tokens = []
            i = 0
            n = len(side)
            while i < n:
                if side[i] in '+-':
                    tokens.append(side[i])
                    i += 1
                    j = i
                    while j < n and side[j] not in '+-':
                        j += 1
                    tokens[-1] += side[i:j]
                    i = j
                else:
                    j = i
                    while j < n and side[j] not in '+-':
                        j += 1
                    tokens.append(side[i:j])
                    i = j

            x_count = 0
            num_sum = 0
            for token in tokens:
                if not token:
                    continue
                if 'x' in token:
                    if token == 'x' or token == '+x':
                        x_count += 1
                    elif token == '-x':
                        x_count -= 1
                    else:
                        coefficient = token.replace('x', '')
                        x_count += int(coefficient)
                else:
                    num_sum += int(token)
            return x_count, num_sum

        left_side, right_side = equation.split('=')
        left_x, left_num = parse_side(left_side)
        right_x, right_num = parse_side(right_side)

        total_x = left_x - right_x
        total_num = right_num - left_num

        if total_x == 0:
            if total_num == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            quotient = total_num // total_x
            return f"x={quotient}"