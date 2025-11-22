import re
from collections import defaultdict
from typing import List


class Term:
    def __init__(self, coefficient, variables):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return "*".join(self.variables) < "*".join(other.variables)

    def __repr__(self):
        if not self.variables:
            return str(self.coefficient)
        return str(self.coefficient) + "*" + "*".join(self.variables)


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
            if new_vars:
                # Evaluate product of variables that may now be numbers
                # safely convert to int multiplication
                new_coeff = 1
                for v in new_vars:
                    if v.isdigit() or (v.startswith('-') and v[1:].isdigit()):
                        new_coeff *= int(v)
                    else:
                        # if non-number remains, treat as variable, so break and skip multiplication
                        new_coeff = None
                        break
                if new_coeff is not None:
                    # All variables were replaced by numbers
                    result.add_term(Term(coeff * new_coeff, []))
                else:
                    # Some variables remain; create term with separated variables and multiplied coeff
                    # Since this is evaluate(), but the pseudocode treats concatenated expression as math expression,
                    # but if any variable remains, just add term as is with multiplied coefficient.
                    # This case is not explicitly handled in pseudocode; safe fallback:
                    result.add_term(Term(coeff, new_vars))
            else:
                result.add_term(Term(coeff, []))
        return result

    def simplify(self):
        simplified_terms = []
        for vars_, coeff in self.terms.items():
            if coeff != 0:
                simplified_terms.append(Term(coeff, list(vars_)))
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        simplified_terms = self.simplify()
        return " + ".join(str(term) for term in simplified_terms)


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
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
            else:  # op == '*'
                output.append(left.multiply(right))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                e = Expression()
                e.add_term(Term(int(token), []))
                output.append(e)
            elif token.isalpha():
                e = Expression()
                coef = var_map.get(token, 1)
                if coef == 1:
                    if token not in var_map:
                        e.add_term(Term(1, [token]))
                    else:
                        e.add_term(Term(1, []))
                else:
                    e.add_term(Term(coef, []))
                output.append(e)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()  # remove '('
            else:  # operator +, -, *
                # precedence handling
                while operators and operators[-1] != '(' and (token in ['+', '-'] or operators[-1] == '*'):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result = []
        for term in simplified_terms:
            if term.variables:
                result.append(str(term.coefficient) + "*" + "*".join(term.variables))
            else:
                result.append(str(term.coefficient))
        return result