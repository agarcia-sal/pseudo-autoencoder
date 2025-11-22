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
        self.terms: Dict[Tuple[str, ...], int] = defaultdict(int)

    def add_term(self, term: Term):
        key = tuple(sorted(term.variables))
        self.terms[key] += term.coefficient

    def multiply(self, other: "Expression") -> "Expression":
        result = Expression()
        for vars1, coeff1 in self.terms.items():
            for vars2, coeff2 in other.terms.items():
                combined_vars = sorted(list(vars1) + list(vars2))
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
                # Evaluate the concatenated new_vars as a multiplication of numbers
                # new_vars might be something like ['2','3','x'], but according to the pseudocode,
                # we concatenate all elements in new_vars and evaluate that.
                # Actually, the pseudocode seems unclear: it says evaluate the concatenation of all elements.
                # We interpret it as multiplication of all numeric elements or strings representing numbers.
                # For example, if new_vars = ['2', '3'], evaluate '2*3' => 6.
                # If variables remain, it means they are not replaced and so coefficient multiplication remains as is.
                # However, pseudocode instructs if new_vars not empty then evaluate concatenation of all elements.
                # To follow pseudocode literally, concatenate and evaluate:

                expr = "*".join(new_vars)
                try:
                    new_coeff = eval(expr)
                except Exception:
                    new_coeff = 1
            else:
                new_coeff = 1
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self) -> List[Term]:
        simplified_terms = [Term(coeff, list(vars_)) for vars_, coeff in self.terms.items() if coeff != 0]
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self) -> str:
        simplified = self.simplify()
        return " + ".join(map(str, simplified))


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        var_map = dict(zip(evalvars, evalints))
        tokens = re.findall(r'\(|\)|\+|\-|\*|\w+', expression)
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
            elif token in ('+', '-', '*'):
                # The precedence handling per pseudocode:
                # While operators is not empty and last operator is not '(',
                # and (token in '+' or '-' or last operator is '*'):
                # then apply_operator.
                # This matches standard precedence: '*' > '+' and '-'.
                while operators and operators[-1] != '(' and \
                        ((token in ('+', '-') or operators[-1] == '*')):
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