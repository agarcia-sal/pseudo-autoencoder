from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace every '-' with '+-' to split properly later, handling leading negatives too
        modified_expression = expression.replace('-', '+-')
        list_of_fractions = modified_expression.split('+')
        filtered_fractions = [frac for frac in list_of_fractions if frac]
        result_fraction = sum(Fraction(frac) for frac in filtered_fractions)
        numerator_part = result_fraction.numerator
        denominator_part = result_fraction.denominator
        return f"{numerator_part}/{denominator_part}"