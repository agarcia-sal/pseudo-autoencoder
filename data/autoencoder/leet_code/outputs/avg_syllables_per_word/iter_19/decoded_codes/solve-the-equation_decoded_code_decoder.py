class Solution:
    def solveEquation(self, equation):
        def parse_side(side):
            # Use a unique separator to split on '+' and '-' while preserving signs
            sep = '#'
            side_modified = side.replace('+', sep + '+').replace('-', sep + '-')
            tokens = side_modified.split(sep)
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
                        numeric_value = int(token.replace('x', ''))
                        x_count += numeric_value
                else:
                    numeric_value = int(token)
                    num_sum += numeric_value
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
            return f"x={division_result}"