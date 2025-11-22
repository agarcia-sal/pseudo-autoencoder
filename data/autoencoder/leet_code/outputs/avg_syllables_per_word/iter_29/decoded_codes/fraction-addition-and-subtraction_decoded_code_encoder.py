from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Replace '-' with '+-' to split expression into terms easily
        modified_expression = expression.replace('-', '+-')
        list_of_fractions = modified_expression.split('+')
        filtered_fractions = [frac for frac in list_of_fractions if frac]

        sum_of_fractions = sum(Fraction(frac) for frac in filtered_fractions)
        numerator_value = sum_of_fractions.numerator
        denominator_value = sum_of_fractions.denominator
        result_string = f"{numerator_value}/{denominator_value}"
        return result_string