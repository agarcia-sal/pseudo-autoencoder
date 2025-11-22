from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        list_of_fractions = self.create_fraction_list(expression)
        result_fraction = self.sum_fractions(list_of_fractions)
        output_string = self.format_fraction_as_string(result_fraction)
        return output_string

    def create_fraction_list(self, expression: str) -> list[Fraction]:
        modified_expression = self.replace_hyphen_with_plus_negative(expression)
        list_of_fraction_strings = self.split_string_by_plus(modified_expression)
        filtered_fraction_strings = self.filter_empty_strings(list_of_fraction_strings)
        fraction_list = self.convert_strings_to_fractions(filtered_fraction_strings)
        return fraction_list

    def replace_hyphen_with_plus_negative(self, expression: str) -> str:
        # Insert '+' before '-' except when the '-' is the first character in the expression
        # This ensures expression like "1/2-1/3" becomes "1/2+-1/3"
        result = []
        for i, ch in enumerate(expression):
            if ch == '-' and i != 0:
                result.append('+')
            result.append(ch)
        return ''.join(result)

    def split_string_by_plus(self, input_string: str) -> list[str]:
        return input_string.split('+')

    def filter_empty_strings(self, list_of_strings: list[str]) -> list[str]:
        return [s for s in list_of_strings if s]

    def convert_strings_to_fractions(self, list_of_fraction_strings: list[str]) -> list[Fraction]:
        fraction_list = []
        for frac_str in list_of_fraction_strings:
            fraction_list.append(Fraction(frac_str))
        return fraction_list

    def sum_fractions(self, list_of_fractions: list[Fraction]) -> Fraction:
        total_fraction = Fraction(0, 1)
        for fraction_element in list_of_fractions:
            total_fraction += fraction_element
        return total_fraction

    def format_fraction_as_string(self, fraction_object: Fraction) -> str:
        numerator_string = str(fraction_object.numerator)
        denominator_string = str(fraction_object.denominator)
        formatted_string = numerator_string + '/' + denominator_string
        return formatted_string