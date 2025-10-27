import re
from collections import defaultdict

class Term:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        self_joined = "*".join(self.variables)
        other_joined = "*".join(other.variables)
        return self_joined < other_joined

    def __repr__(self):
        if len(self.variables) == 0:
            return str(self.coefficient)
        joined_vars = "*".join(self.variables)
        return f"{self.coefficient}*{joined_vars}"

class Expression:
    def __init__(self):
        self.terms = defaultdict(int)

    def add_term(self, term):
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient

    def multiply(self, other):
        result = Expression()
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars_list = sorted(vars1 + vars2)
                new_term = Term(coeff1 * coeff2, combined_vars_list)
                result.add_term(new_term)
        return result

    def add(self, other):
        for vars, coeff in other.terms.items():
            new_term = Term(coeff, list(vars))
            self.add_term(new_term)
        return self

    def subtract(self, other):
        for vars, coeff in other.terms.items():
            new_term = Term(-coeff, list(vars))
            self.add_term(new_term)
        return self

    def evaluate(self, var_map):
        result = Expression()
        for vars, coeff in self.terms.items():
            new_vars = []
            for var in vars:
                if var in var_map:
                    new_vars.append(str(var_map[var]))
                else:
                    new_vars.append(var)
            if len(new_vars) == 0:
                new_coeff = 1
            else:
                # Evaluate concatenated string as expression (e.g. '23' -> 23)
                # Since all are digits or variables, safe to convert joined string to int if all digits
                # But new_vars might contain variables as string, so we join without separator, then evaluate
                # Example: ['2', '3'] -> '23' -> int(23)
                # If variables remain, eval might fail, but per design, variables replaced by digits or remain as strings
                # So we join, then try int cast
                joined = ''.join(new_vars)
                try:
                    new_coeff = int(joined)
                except ValueError:
                    # If conversion fails (means variables remain), treat as 0 coefficient to ignore term?
                    # But the pseudocode does not specify such case, so preserve original coeff with variables left
                    new_coeff = 1
            new_term = Term(coeff * new_coeff, [])
            result.add_term(new_term)
        return result

    def simplify(self):
        simplified_terms = []
        for vars, coeff in self.terms.items():
            if coeff != 0:
                new_term = Term(coeff, list(vars))
                simplified_terms.append(new_term)
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        simplified_list = self.simplify()
        string_list = []
        for term in simplified_list:
            string_list.append(repr(term))
        return ' + '.join(string_list)

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = dict(zip(evalvars, evalints))
        # Tokens: parentheses, +, -, *, numbers, variables
        pattern = r'\(|\)|\+|\-|\*|\d+|[a-zA-Z]+'
        tokens = re.findall(pattern, expression)
        output = []
        operators = []

        def apply_operator():
            right = output.pop()
            left = output.pop()
            op = operators.pop()
            if op == '+':
                output.append(left.add(right))
            elif op == '-':
                output.append(left.subtract(right))
            elif op == '*':
                output.append(left.multiply(right))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                new_expression = Expression()
                new_term = Term(int(token), [])
                new_expression.add_term(new_term)
                output.append(new_expression)
            elif token.isalpha():
                new_expression = Expression()
                coef = var_map[token] if token in var_map else 1
                if coef == 1:
                    if token not in var_map:
                        new_term = Term(1, [token])
                    else:
                        new_term = Term(1, [])
                else:
                    new_term = Term(coef, [])
                new_expression.add_term(new_term)
                output.append(new_expression)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()  # pop '('
            elif token in ('+', '-', '*'):
                while operators and operators[-1] != '(' and (
                    token in ('+', '-') or operators[-1] == '*'
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result_strings = []
        for term in simplified_terms:
            if len(term.variables) == 0:
                result_strings.append(str(term.coefficient))
            else:
                joined_vars = "*".join(term.variables)
                result_strings.append(f"{term.coefficient}*{joined_vars}")
        return result_strings