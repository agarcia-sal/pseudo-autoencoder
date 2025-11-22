from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Insert '+' before every '-' to split easily by '+'
        modified_expression = expression.replace('-', '+-')
        # Split by '+' to get fractions or empty strings
        fractions = modified_expression.split('+')
        # Filter out empty strings
        filtered_fractions = [f for f in fractions if f]
        sum_result = Fraction(0, 1)
        for fraction_string in filtered_fractions:
            sum_result += Fraction(fraction_string)
        return f"{sum_result.numerator}/{sum_result.denominator}"