import re
from collections import defaultdict
from typing import List, Dict, Tuple


class Term:
    def __init__(self, coefficient: int, variables: List[str]):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other: 'Term') -> bool:
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return '*'.join(self.variables) < '*'.join(other.variables)

    def __repr__(self) -> str:
        if len(self.variables) == 0:
            return str(self.coefficient)
        return str(self.coefficient) + '*' + '*'.join(self.variables)


class Expression:
    def __init__(self):
        # keys: tuple of vars sorted, values: integer coefficient
        self.terms: Dict[Tuple[str, ...], int] = defaultdict(int)

    def add_term(self, term: Term) -> None:
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient
        if self.terms[key] == 0:
            del self.terms[key]

    def multiply(self, other: 'Expression') -> 'Expression':
        result = Expression()
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars = sorted(vars1 + vars2)
                result.add_term(Term(coeff1 * coeff2, combined_vars))
        return result

    def add(self, other: 'Expression') -> 'Expression':
        for vars_, coeff in other.terms.items():
            self.add_term(Term(coeff, list(vars_)))
        return self

    def subtract(self, other: 'Expression') -> 'Expression':
        for vars_, coeff in other.terms.items():
            self.add_term(Term(-coeff, list(vars_)))
        return self

    def evaluate(self, var_map: Dict[str, int]) -> 'Expression':
        result = Expression()
        for vars_, coeff in self.terms.items():
            new_vars = []
            for var in vars_:
                if var in var_map:
                    new_vars.append(str(var_map[var]))
                else:
                    new_vars.append(var)
            if len(new_vars) == 0:
                new_coeff = 1
            else:
                expr_str = '*'.join(new_vars)
                # Safely evaluate arithmetic expression that consists of ints and '*'
                parts = expr_str.split('*')
                # convert parts to ints after confirming all are digits (should be true)
                prod = 1
                for part in parts:
                    # If any part is a variable, treat it as 1 (should not happen here)
                    if part.isdigit() or (part.startswith('-') and part[1:].isdigit()):
                        prod *= int(part)
                    else:
                        prod = 0
                        break
                new_coeff = prod
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self) -> List[Term]:
        simplified_terms = [
            Term(coeff, list(vars_)) for vars_, coeff in self.terms.items() if coeff != 0
        ]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self) -> str:
        return '+'.join(map(str, self.simplify()))


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        var_map = dict(zip(evalvars, evalints))
        # Tokenize input expression:
        # tokens can be parentheses, operators (+,-,*), numbers, or variables(letters)
        tokens = re.findall(
            r'\(|\)|\+|\-|\*|\d+|[a-zA-Z]+', expression
        )
        output: List[Expression] = []
        operators: List[str] = []

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
        n = len(tokens)

        while i < n:
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
            elif token in {'+', '-', '*'}:
                # Operator precedence:
                # '*' highest, then '+', '-'
                # While top operator is '*' or same precedence as token, apply
                while (
                    operators
                    and operators[-1] != '('
                    and (
                        token in {'+', '-'}
                        or operators[-1] == '*'
                    )
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result = []
        for term in simplified_terms:
            if len(term.variables) == 0:
                result.append(str(term.coefficient))
            else:
                result.append(str(term.coefficient) + '*' + '*'.join(term.variables))
        return result