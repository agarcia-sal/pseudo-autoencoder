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
        else:
            return "*".join(self.variables) < "*".join(other.variables)

    def __repr__(self) -> str:
        if not self.variables:
            return str(self.coefficient)
        else:
            return f"{self.coefficient}*{'*'.join(self.variables)}"


class Expression:
    def __init__(self):
        self.terms: Dict[Tuple[str, ...], int] = defaultdict(int)

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
                new_coeff = eval("*".join(new_vars))
            else:
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
        return " + ".join(map(str, self.simplify()))


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        var_map = dict(zip(evalvars, evalints))
        tokens = re.findall(r"\w+|[()+\-*]", expression)
        output: List[Expression] = []
        operators: List[str] = []

        def apply_operator() -> None:
            right = output.pop()
            left = output.pop()
            op = operators.pop()
            if op == "+":
                output.append(left.add(right))
            elif op == "-":
                output.append(left.subtract(right))
            elif op == "*":
                output.append(left.multiply(right))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                exp = Expression()
                exp.add_term(Term(int(token), []))
                output.append(exp)
            elif token.isalpha():
                exp = Expression()
                coef = var_map.get(token, None)
                if coef is None:
                    exp.add_term(Term(1, [token]))
                else:
                    exp.add_term(Term(coef, []))
                output.append(exp)
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    apply_operator()
                operators.pop()  # remove '('
            elif token in "+-*":
                while (
                    operators
                    and operators[-1] != "("
                    and (token in "+-" or operators[-1] == "*")
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        return [
            str(term.coefficient)
            if not term.variables
            else str(term.coefficient) + "*" + "*".join(term.variables)
            for term in simplified_terms
        ]