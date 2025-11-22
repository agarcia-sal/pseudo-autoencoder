import re
from collections import defaultdict
from typing import List, Dict, Tuple, Union


class Term:
    def __init__(self, coefficient: int, variables: List[str]):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other: 'Term') -> bool:
        # Compare by number of variables (longer first)
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        # Then lex order by variables joined with '*'
        return '*'.join(self.variables) < '*'.join(other.variables)

    def __repr__(self) -> str:
        if not self.variables:
            return str(self.coefficient)
        return str(self.coefficient) + '*' + '*'.join(self.variables)


class Expression:
    def __init__(self):
        self.terms: Dict[Tuple[str, ...], int] = defaultdict(int)

    def add_term(self, term: Term) -> None:
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient

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
            # Evaluate numeric expression if possible
            if not new_vars:  # no variables left, pure coefficient
                new_coeff = 1
            else:
                # The expression to evaluate, e.g. '2*3*4' or '2*X*3'
                # Only numeric strings in new_vars should be evaluated
                # The expression can contain variables, which should remain
                # But here, per pseudocode, all replaced with values or keep var,
                # then numeric parts joined and evaluated.
                # According to pseudocode, numeric expressions get evaluated.
                # So if new_vars contains any variable (non digit) left,
                # can't evaluate - but per pseudocode, no such complexity.
                # Since all variables replaced as string of their values if possible,
                # else kept as variable name, so evaluate only if all numeric.
                if all(re.fullmatch(r'\d+', nv) for nv in new_vars):
                    expr_str = '*'.join(new_vars)
                    new_coeff = eval(expr_str)
                else:
                    # can't evaluate, treat as coefficient 1 but variables remain (?)
                    # But pseudocode sets variables list empty, so this shouldn't happen.
                    # To be consistent with pseudocode: Set new_coeff = 1 and variables empty.
                    new_coeff = 1
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self) -> List[Term]:
        simplified_terms = [
            Term(coeff, list(vars_))
            for vars_, coeff in self.terms.items()
            if coeff != 0
        ]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self) -> str:
        return ' '.join(str(term) for term in self.simplify())


class Solution:
    def basicCalculatorIV(
        self,
        expression: str,
        evalvars: List[str],
        evalints: List[int]
    ) -> List[str]:
        var_map = dict(zip(evalvars, evalints))
        # Token patterns
        token_pattern = re.compile(
            r'\(|\)|\+|\-|\*|\d+|\w+'
        )
        tokens = token_pattern.findall(expression)

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
                operators.pop()  # remove '('
            elif token in ['+', '-', '*']:
                # Operator precedence:
                # We apply operators on the stack while:
                # - top operator is not '('
                # - and (token is '+' or '-') or top operator is '*'
                #
                # This matches precedence rules:
                # '*' > '+'/'-'
                #
                while (
                    operators and operators[-1] != '(' and
                    (token in ['+', '-'] or operators[-1] == '*')
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        # Return formatted strings as per instructions:
        # coefficient*var1*var2 if variables else coefficient as string
        return [
            str(term.coefficient) + ('*' + '*'.join(term.variables) if term.variables else '')
            for term in simplified_terms
        ]