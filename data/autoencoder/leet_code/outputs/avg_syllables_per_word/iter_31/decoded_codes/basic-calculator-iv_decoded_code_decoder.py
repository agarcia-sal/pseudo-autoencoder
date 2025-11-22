import re
from collections import defaultdict
from typing import List, Dict, Tuple


class Term:
    def __init__(self, coefficient: int, variables: List[str]):
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other: "Term") -> bool:
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        return "*".join(self.variables) < "*".join(other.variables)

    def __repr__(self) -> str:
        if not self.variables:
            return str(self.coefficient)
        return str(self.coefficient) + "*" + "*".join(self.variables)


class Expression:
    def __init__(self):
        self.terms = defaultdict(int)  # Dict[Tuple[str, ...], int]

    def add_term(self, term: Term) -> None:
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient

    def multiply(self, other: "Expression") -> "Expression":
        result = Expression()
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars = sorted(vars1 + vars2)
                result.add_term(Term(coeff1 * coeff2, combined_vars))
        return result

    def add(self, other: "Expression") -> "Expression":
        for vars_, coeff in other.terms.items():
            self.add_term(Term(coeff, list(vars_)))
        return self

    def subtract(self, other: "Expression") -> "Expression":
        for vars_, coeff in other.terms.items():
            self.add_term(Term(-coeff, list(vars_)))
        return self

    def evaluate(self, var_map: Dict[str, int]) -> "Expression":
        result = Expression()
        for vars_, coeff in self.terms.items():
            new_vars = []
            for var in vars_:
                if var in var_map:
                    new_vars.append(str(var_map[var]))
                else:
                    new_vars.append(var)
            if new_vars:
                expr_str = "*".join(new_vars)
                # Evaluate the expression as arithmetic multiplying all numbers
                # variables remain as is (strings), so we split and multiply integers only
                factors = expr_str.split("*")
                new_coeff = 1
                variables_after_eval = []
                for f in factors:
                    if f.isdigit() or (f.startswith('-') and f[1:].isdigit()):
                        new_coeff *= int(f)
                    else:
                        variables_after_eval.append(f)
                # Add term: coefficient * new_coeff, variables_after_eval sorted
                result.add_term(Term(coeff * new_coeff, variables_after_eval))
            else:
                # No variables means just multiply coefficient by 1
                result.add_term(Term(coeff * 1, []))
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
        return "+".join(str(term) for term in self.simplify())


class Solution:
    def basicCalculatorIV(
        self,
        expression: str,
        variables: List[str],
        evalvars: List[str],
        evalints: List[int],
    ) -> List[str]:
        var_map = dict(zip(evalvars, evalints))

        tokens = self.tokenize(expression)
        output = []
        operators = []

        def apply_operator():
            right = output.pop()
            left = output.pop()
            op = operators.pop()
            if op == "+":
                output.append(left.add(right))
            elif op == "-":
                output.append(left.subtract(right))
            else:  # '*'
                output.append(left.multiply(right))

        i = 0
        n = len(tokens)
        while i < n:
            token = tokens[i]
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                # number
                e = Expression()
                e.add_term(Term(int(token), []))
                output.append(e)
            elif token.isalpha():
                e = Expression()
                coef = var_map.get(token, 1)
                if coef == 1 and token not in var_map:
                    e.add_term(Term(1, [token]))
                else:
                    e.add_term(Term(coef, []))
                output.append(e)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    apply_operator()
                if operators:
                    operators.pop()  # remove '('
            else:  # operator + - *
                # precedence: * > + -
                # while top of stack is not '(' and has precedence >= current token
                while (
                    operators
                    and operators[-1] != "("
                    and (token in ("+", "-") or operators[-1] == "*")
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        res = []
        for term in simplified_terms:
            if term.variables:
                res.append(str(term.coefficient) + "*" + "*".join(term.variables))
            else:
                res.append(str(term.coefficient))
        return res

    token_pattern = re.compile(r'\d+|[a-z]+|[()+\-*]')

    def tokenize(self, expression: str) -> List[str]:
        # Extract tokens: numbers, words, parentheses, operators
        # The regex handles numbers, alphabetic variables, and single-char tokens
        tokens = self.token_pattern.findall(expression.replace(' ', ''))
        return tokens