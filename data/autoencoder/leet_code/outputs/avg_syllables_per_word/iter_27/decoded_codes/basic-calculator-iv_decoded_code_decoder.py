import collections
import re
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
        self.terms = collections.defaultdict(int)  # key: tuple of variables, value: coefficient

    def add_term(self, term: Term):
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
                # Evaluate combined variables concatenated by "*"
                # The new_vars list can contain string representations of integers or variables
                # We interpret digits strings as integers, otherwise variables remain
                # Evaluate the product of integer constants in new_vars
                # Variables remain as is; but problem states new_vars is a list of strings - if there are digits, multiply them, else count as variables.
                # Actually the pseudocode says "EVALUATION OF the CONCATENATION OF new_vars AS STRINGS"
                # So we have something like ['2','3'] -> evaluate '23' = 23? That would be wrong logically.
                # But the pseudocode must mean numerical multiplication of values for variables replaced.
                # To keep faith, we will multiply all numeric values in new_vars and keep non-numeric vars.
                numeric_coef = 1
                filtered_vars = []
                for item in new_vars:
                    if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                        numeric_coef *= int(item)
                    else:
                        filtered_vars.append(item)
                new_coeff = numeric_coef
                new_vars = filtered_vars
            else:
                new_coeff = 1
            result.add_term(Term(coeff * new_coeff, new_vars))
        return result

    def simplify(self) -> List[Term]:
        simplified_terms = []
        for vars_, coeff in self.terms.items():
            if coeff != 0:
                simplified_terms.append(Term(coeff, list(vars_)))
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self) -> str:
        return " + ".join(repr(term) for term in self.simplify())


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        var_map = dict(zip(evalvars, evalints))
        # Token pattern matches: parentheses, operators, numbers, or variables
        token_pattern = re.compile(
            r"\(|\)|\+|\-|\*|\d+|\w+"
        )  # open paren, close paren, plus, minus, asterisk, digits, word characters
        tokens_raw = token_pattern.findall(expression)
        # Map tokens to descriptive strings for clarity following pseudocode
        tokens = []
        for t in tokens_raw:
            if t == "(":
                tokens.append("open parenthesis")
            elif t == ")":
                tokens.append("close parenthesis")
            elif t == "+":
                tokens.append("plus")
            elif t == "-":
                tokens.append("minus")
            elif t == "*":
                tokens.append("asterisk")
            elif t.isdigit():
                tokens.append(t)
            else:
                # variable token
                tokens.append(t)

        output: List[Expression] = []
        operators: List[str] = []

        def apply_operator():
            right = output.pop()
            left = output.pop()
            op = operators.pop()
            if op == "plus":
                output.append(left.add(right))
            elif op == "minus":
                output.append(left.subtract(right))
            elif op == "asterisk":
                output.append(left.multiply(right))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                expr = Expression()
                expr.add_term(Term(int(token), []))
                output.append(expr)
            elif token.isalpha() or (token[0].isalpha() and token.isalnum()):
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
            elif token == "open parenthesis":
                operators.append(token)
            elif token == "close parenthesis":
                while operators and operators[-1] != "open parenthesis":
                    apply_operator()
                if operators and operators[-1] == "open parenthesis":
                    operators.pop()
            elif token in {"plus", "minus", "asterisk"}:
                # Operator precedence: '*' > '+'/'-'
                # While top operator is not '(' and (current token in '+'/'-' or top operator is '*'), apply operator
                while (
                    operators
                    and operators[-1] != "open parenthesis"
                    and (
                        token in {"plus", "minus"}
                        or operators[-1] == "asterisk"
                    )
                ):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result_list = []
        for term in simplified_terms:
            if term.variables:
                result_list.append(str(term.coefficient) + "*" + "*".join(term.variables))
            else:
                result_list.append(str(term.coefficient))
        return result_list