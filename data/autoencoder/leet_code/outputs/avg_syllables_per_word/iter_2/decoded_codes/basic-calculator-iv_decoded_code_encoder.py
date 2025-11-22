from collections import defaultdict
import re

class Term:
    def __init__(self, coefficient: int, variables: list[str]):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return '*'.join(self.variables) < '*'.join(other.variables)

    def __repr__(self):
        if not self.variables:
            return str(self.coefficient)
        return f"{self.coefficient}*{'*'.join(self.variables)}"

class Expression:
    def __init__(self):
        self.terms = defaultdict(int)

    def add_term(self, term: Term):
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
            if new_vars:
                # Evaluate product of new_vars (may contain numbers and variables as strings)
                # If all are digits, multiply as integers, else treat as string with '*'
                try:
                    new_coeff = 1
                    for v in new_vars:
                        # v might be a variable name or a number string
                        new_coeff *= int(v)
                except ValueError:
                    # If not all digits, cannot compute - treat as variables - fallback
                    new_coeff = 1
                    for v in new_vars:
                        # This situation can't happen if we substituted known vars
                        # but per pseudocode fallback is 1
                        pass
                result.add_term(Term(coeff * new_coeff, []))
            else:
                new_coeff = 1
                result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self):
        simplified_terms = [Term(coeff, list(vars)) for vars, coeff in self.terms.items() if coeff != 0]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return ' + '.join(str(term) for term in self.simplify())

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
        var_map = dict(zip(evalvars, evalints))
        # tokenize: parentheses, operators +-* , numbers (digits+), words (vars)
        tokens = re.findall(r'\(|\)|\+|\-|\*|\d+|[a-z]+', expression)
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
                new_exp = Expression()
                new_exp.add_term(Term(int(token), []))
                output.append(new_exp)
            elif token.isalpha():
                new_exp = Expression()
                coef = var_map.get(token, 1)
                if coef == 1:
                    if token not in var_map:
                        new_exp.add_term(Term(1, [token]))
                    else:
                        new_exp.add_term(Term(1, []))
                else:
                    new_exp.add_term(Term(coef, []))
                output.append(new_exp)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()
            elif token in '+-*':
                # precedence: * > +/-
                while operators and operators[-1] != '(' and (token in '+-' or operators[-1] == '*'):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()

        result = []
        for term in simplified_terms:
            if term.variables:
                result.append(f"{term.coefficient}*{'*'.join(term.variables)}")
            else:
                result.append(str(term.coefficient))
        return result