from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        replaced_expression = expression.replace('-', '+-')
        fractions_list = replaced_expression.split('+')
        filtered_fractions = [frac for frac in fractions_list if frac]

        total = Fraction(0, 1)
        for frac in filtered_fractions:
            total += Fraction(frac)

        return f"{total.numerator}/{total.denominator}"