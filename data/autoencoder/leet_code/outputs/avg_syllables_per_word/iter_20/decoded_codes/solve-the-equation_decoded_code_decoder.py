class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side: str):
            # Replace '+' with '#+' and '-' with '#-' to split tokens easily
            # Note: We add '#' prefix only for '+' and '-' not at start to handle leading tokens
            # So first ensure side starts with '+' or '-' or else prepend '+'
            if not side or side[0] not in '+-':
                side = '+' + side
            tokens = []
            i = 0
            while i < len(side):
                sign = side[i]
                i += 1
                start = i
                while i < len(side) and side[i] not in '+-':
                    i += 1
                tokens.append(sign + side[start:i])

            x_count = 0
            num_sum = 0
            for token in tokens:
                if not token:
                    continue
                if 'x' in token:
                    # Handle cases:
                    # token can be +x, -x, +2x, -3x etc.
                    coeff_str = token[:-1]  # remove the 'x'
                    if coeff_str == '+' or coeff_str == '':
                        x_count += 1
                    elif coeff_str == '-':
                        x_count -= 1
                    else:
                        try:
                            x_count += int(coeff_str)
                        except ValueError:
                            # Invalid coefficient, treat as zero contribution
                            pass
                else:
                    try:
                        num_sum += int(token)
                    except ValueError:
                        pass
            return x_count, num_sum

        if equation.count('=') != 1:
            # Malformed input (no or multiple '='), no solution
            return "No solution"

        left_side, right_side = equation.split('=', 1)
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