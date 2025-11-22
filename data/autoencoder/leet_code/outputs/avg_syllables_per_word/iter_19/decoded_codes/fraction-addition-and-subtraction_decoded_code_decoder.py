from fractions import Fraction

class Solution:
    def fractionAddition(self, expression):
        # Replace '-' with '+-' to standardize splitting
        modified_expression = expression.replace('-', '+-')
        fractions_list = modified_expression.split('+')
        filtered_fractions = [f for f in fractions_list if f]
        result_fraction = sum(Fraction(frac) for frac in filtered_fractions)
        return f"{result_fraction.numerator}/{result_fraction.denominator}"