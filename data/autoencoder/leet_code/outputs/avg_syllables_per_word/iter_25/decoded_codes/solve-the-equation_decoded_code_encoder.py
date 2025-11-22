class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side: str):
            # Replace '+' with '#+' and '-' with '#-' to split tokens cleanly
            # Note: the first token might be empty if side starts with '+', so handle that
            tokens = side.replace('+', '#+').replace('-', '#-').split('#')
            x_count = 0
            num_sum = 0
            for token in tokens:
                if token == '':
                    continue
                if 'x' in token:
                    if token == 'x' or token == '+x':
                        x_count += 1
                    elif token == '-x':
                        x_count -= 1
                    else:
                        number_string = token.replace('x', '')
                        x_count += int(number_string)
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
            division_result = total_num // total_x
            return "x=" + str(division_result)