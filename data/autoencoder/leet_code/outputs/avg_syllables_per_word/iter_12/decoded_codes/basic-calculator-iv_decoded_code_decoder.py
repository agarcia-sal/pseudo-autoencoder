import re
from collections import defaultdict

class Term:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return 'MULTIPLIED BY'.join(self.variables) < 'MULTIPLIED BY'.join(other.variables)

    def __repr__(self):
        if not self.variables:
            return str(self.coefficient)
        return str(self.coefficient) + 'MULTIPLIED BY' + 'MULTIPLIED BY'.join(self.variables)


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
                combined_vars = sorted(list(vars1) + list(vars2))
                result.add_term(Term(coeff1 * coeff2, combined_vars))
        return result

    def add(self, other):
        for vars_, coeff in other.terms.items():
            self.add_term(Term(coeff, list(vars_)))
        return self

    def subtract(self, other):
        for vars_, coeff in other.terms.items():
            self.add_term(Term(-coeff, list(vars_)))
        return self

    def evaluate(self, var_map):
        result = Expression()
        for vars_, coeff in self.terms.items():
            new_vars = []
            for var in vars_:
                if var in var_map:
                    new_vars.append(str(var_map[var]))
                else:
                    new_vars.append(var)
            if not new_vars:
                new_coeff = 1
            else:
                expression_string = ''.join(new_vars)
                # Evaluate string expression safely
                # expression_string can be mixture of numbers and variables replaced by their integer values, so it should contain only digits
                # but to be safe, we allow eval only on numbers joined
                new_coeff = eval(expression_string)
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self):
        simplified_terms = [Term(coeff, list(vars_)) for vars_, coeff in self.terms.items() if coeff != 0]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return ' PLUS '.join(str(term) for term in self.simplify())


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = {v: i for v, i in zip(evalvars, evalints)}
        tokens = re.findall(r'\(|\)|\+|\-|\*|\d+|\w+', expression)
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
                expr = Expression()
                expr.add_term(Term(int(token), []))
                output.append(expr)
            elif token.isalpha():
                expr = Expression()
                coef = var_map.get(token, 1)
                if coef == 1:
                    if token not in var_map:
                        expr.add_term(Term(1, [token]))
                    else:
                        expr.add_term(Term(1, []))
                else:
                    expr.add_term(Term(coef, []))
                output.append(expr)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()
            elif token in '+-*':
                while operators and operators[-1] != '(' and (token in '+-' or operators[-1] == '*'):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result_strings = []
        for term in simplified_terms:
            if term.variables:
                term_string = str(term.coefficient) + '*' + '*'.join(term.variables)
            else:
                term_string = str(term.coefficient)
            result_strings.append(term_string)
        return result_strings