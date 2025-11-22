import re
from collections import defaultdict

class Term:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        self_joined = '*'.join(self.variables)
        other_joined = '*'.join(other.variables)
        return self_joined < other_joined

    def __repr__(self):
        if len(self.variables) == 0:
            return str(self.coefficient)
        return str(self.coefficient) + '*' + '*'.join(self.variables)


class Expression:
    def __init__(self):
        self.terms = defaultdict(int)

    def add_term(self, term):
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient

    def multiply(self, other):
        result = Expression()
        for key_vars_one, value_coeff_one in self.terms.items():
            for key_vars_two, value_coeff_two in other.terms.items():
                combined_vars_list = sorted(list(key_vars_one) + list(key_vars_two))
                result.add_term(Term(value_coeff_one * value_coeff_two, combined_vars_list))
        return result

    def add(self, other):
        for key_vars, value_coeff in other.terms.items():
            self.add_term(Term(value_coeff, list(key_vars)))
        return self

    def subtract(self, other):
        for key_vars, value_coeff in other.terms.items():
            self.add_term(Term(-value_coeff, list(key_vars)))
        return self

    def evaluate(self, var_map):
        result = Expression()
        for key_vars, value_coeff in self.terms.items():
            new_vars_list = []
            for variable in key_vars:
                if variable in var_map:
                    new_vars_list.append(str(var_map[variable]))
                else:
                    new_vars_list.append(variable)
            if len(new_vars_list) == 0:
                new_coefficient = 1
            else:
                expression_string = ''.join(new_vars_list)
                # Safely evaluate the expression string, which consists only of numbers and variables replaced by numbers
                # Since all variables replaced are replaced by numbers, expression_string is just digits concatenated. So just int().
                # But the pseudocode hints at "evaluation" so handle multi-digit accordingly.
                # To be safe, use int conversion as expression_string should be string of digits.
                new_coefficient = int(expression_string)
            result.add_term(Term(value_coeff * new_coefficient, []))
        return result

    def simplify(self):
        simplified_terms = [Term(value_coeff, list(key_vars)) for key_vars, value_coeff in self.terms.items() if value_coeff != 0]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return ' + '.join(map(repr, self.simplify()))


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = dict(zip(evalvars, evalints))
        # Tokenize expression
        # Tokens are parentheses, plus, minus, asterisk, digits, word characters
        tokens = re.findall(r'\(|\)|\+|\-|\*|\d+|\w+', expression)
        output = []
        operators = []

        def apply_operator():
            right_operand = output.pop()
            left_operand = output.pop()
            operator = operators.pop()
            if operator == '+':
                output.append(left_operand.add(right_operand))
            elif operator == '-':
                output.append(left_operand.subtract(right_operand))
            elif operator == '*':
                output.append(left_operand.multiply(right_operand))

        index = 0
        while index < len(tokens):
            token = tokens[index]
            if token.isdigit():
                e = Expression()
                e.add_term(Term(int(token), []))
                output.append(e)
            elif token.isalpha():
                e = Expression()
                coefficient_value = var_map.get(token, 1)
                if coefficient_value == 1:
                    if token not in var_map:
                        e.add_term(Term(1, [token]))
                    else:
                        e.add_term(Term(1, []))
                else:
                    e.add_term(Term(coefficient_value, []))
                output.append(e)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()  # remove '('
            elif token in ('+', '-', '*'):
                while (operators and operators[-1] != '(' and
                       (token in ('+', '-') or operators[-1] == '*')):
                    apply_operator()
                operators.append(token)
            index += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result_strings = []
        for term in simplified_terms:
            if len(term.variables) > 0:
                term_string = str(term.coefficient) + '*' + '*'.join(term.variables)
                result_strings.append(term_string)
            else:
                result_strings.append(str(term.coefficient))
        return result_strings