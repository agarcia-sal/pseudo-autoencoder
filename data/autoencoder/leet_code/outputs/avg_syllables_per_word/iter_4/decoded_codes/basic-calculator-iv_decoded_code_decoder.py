import re
from collections import defaultdict

class Term:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return '*'.join(self.variables) < '*'.join(other.variables)

    def __repr__(self):
        if not self.variables:
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
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars = sorted(vars1 + vars2)
                result.add_term(Term(coeff1 * coeff2, combined_vars))
        return result

    def add(self, other):
        for vars, coeff in other.terms.items():
            self.add_term(Term(coeff, list(vars)))
        return self

    def subtract(self, other):
        for vars, coeff in other.terms.items():
            self.add_term(Term(-coeff, list(vars)))
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
            if new_vars and all(x.isdigit() for x in new_vars):
                new_coeff = 1
                for val in new_vars:
                    new_coeff *= int(val)
            elif new_vars and any(not x.isdigit() for x in new_vars):
                # Variables remain, cannot fully evaluate numeric product
                # Treat numeric strings as coefficients multiplied
                numeric_part = 1
                vars_part = []
                for val in new_vars:
                    if val.isdigit():
                        numeric_part *= int(val)
                    else:
                        vars_part.append(val)
                result.add_term(Term(coeff * numeric_part, vars_part))
                continue
            else:
                new_coeff = 1
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self):
        simplified_terms = []
        for vars, coeff in self.terms.items():
            if coeff != 0:
                simplified_terms.append(Term(coeff, list(vars)))
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return ' + '.join(map(repr, self.simplify()))


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = dict(zip(evalvars, evalints))
        tokens = re.findall(r'\(|\)|\+|\-|\*|\d+|[a-zA-Z]+', expression)
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
            else:  # op == '*'
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
                coef = var_map.get(token, None)
                if coef is None:
                    expr.add_term(Term(1, [token]))
                else:
                    if coef == 1:
                        expr.add_term(Term(1, []))
                    else:
                        expr.add_term(Term(coef, []))
                output.append(expr)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()  # Remove '('
            elif token in '+-*':
                while (operators and operators[-1] != '(' and
                       (token in '+-' or operators[-1] == '*')):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result = []
        for term in simplified_terms:
            if term.variables:
                result.append(str(term.coefficient) + '*' + '*'.join(term.variables))
            else:
                result.append(str(term.coefficient))
        return result