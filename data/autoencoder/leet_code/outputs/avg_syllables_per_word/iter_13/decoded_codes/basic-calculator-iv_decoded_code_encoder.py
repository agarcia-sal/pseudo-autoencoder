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
        if self.terms[key] == 0:
            del self.terms[key]

    def multiply(self, other):
        result = Expression()
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars = sorted(vars1 + vars2)
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
            if new_vars:
                # Evaluate expression of concatenated factors separated by '*'
                # For example: vars could be ['2','3','x'] means "2*3*x"
                # But 'x' is not numeric, so eval on '2*3*x' would fail
                # Instead, the problem logic seems to consider variables replaced by numbers only
                # and any leftover variable means term is not fully evaluated.
                # So, here it seems only variables that exist in var_map are replaced by their number,
                # and after that, we evaluate numeric-only terms.
                # If any non-digit remains, skip evaluating coefficient numerically.
                # But per pseudocode, if new_vars is not empty, "new_coeff" is the evaluation of concatenation of elements of new_vars as math expr.
                # We implement that carefully by checking if after replacement all are digits.
                expr_str = '*'.join(new_vars)
                # Only evaluate if expr_str is digits and operators (i.e. safe)
                # Since separated by '*', a safe eval can be done.
                # We'll use eval with a restricted builtins for safety here.
                try:
                    new_coeff = eval(expr_str, {"__builtins__": None}, {})
                except:
                    new_coeff = 1
            else:
                new_coeff = 1
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self):
        simplified_terms = [Term(coeff, list(vars_)) for vars_, coeff in self.terms.items() if coeff != 0]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return ' '.join(map(str, self.simplify()))

class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = dict(zip(evalvars, evalints))
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
                coef = var_map[token] if token in var_map else 1
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
                operators.pop()  # remove '('
            elif token in ['+', '-', '*']:
                # Based on operator precedence: '*' > '+' and '-'
                # While top operator has higher or equal precedence, apply it.
                while (operators and operators[-1] != '(' and
                       (token in ['+', '-'] or operators[-1] == '*')):
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