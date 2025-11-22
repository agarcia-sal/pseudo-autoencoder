import re
from collections import defaultdict

class Term:
    def __init__(self, coefficient, variables):
        # coefficient: int
        # variables: List[str] (sorted later when used as key)
        self.coefficient = coefficient
        self.variables = variables

    def __lt__(self, other):
        # If lengths differ, longer length considered smaller (comes first)
        if len(self.variables) != len(other.variables):
            return len(self.variables) > len(other.variables)
        # If lengths equal, compare lex order of joined vars with '*'
        return "*".join(self.variables) < "*".join(other.variables)

    def __repr__(self):
        if len(self.variables) == 0:
            return str(self.coefficient)
        return str(self.coefficient) + "*" + "*".join(self.variables)


class Expression:
    def __init__(self):
        self.terms = defaultdict(int)  # key: tuple(vars), value: coefficient

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
                    # Append string representation of mapped value to new_vars
                    new_vars.append(str(var_map[var]))
                else:
                    new_vars.append(var)
            if len(new_vars) == 0:
                new_coeff = 1
            else:
                # Concatenate elements without separator and eval as expression
                # Since new_vars may contain digits or strings
                # Example: ['2','3'] -> '23' as string, but we want multiplication?
                # But problem states: evaluation of concatenated new_vars string
                # For example: If new_vars = ['2','3'], concatenation is '23', eval('23') = 23
                # If new_vars = ['a','b'], eval will be invalid - but a,b replaced by digits or remain unchanged?
                # Since if variable not in var_map, kept as string, so eval might be invalid.
                # So per pseudocode, new_vars elements replaced by their mapped values if in var_map else remain variables.
                # If variables remain, concatenate string would be invalid to eval.
                # So if any variable remains alphabetic in new_vars, eval would fail.
                # Problem does not specify this branch explicitly.
                # So we trust all remaining variables are numeric strings.
                # So join variables by empty string and eval.
                expr = "".join(new_vars)
                # eval string safely as int
                new_coeff = eval(expr)
            result.add_term(Term(coeff * new_coeff, []))
        return result

    def simplify(self):
        simplified_terms = []
        for vars_, coeff in self.terms.items():
            if coeff != 0:
                simplified_terms.append(Term(coeff, list(vars_)))
        simplified_terms.sort()
        return simplified_terms

    def __repr__(self):
        return " + ".join(repr(term) for term in self.simplify())


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        var_map = dict(zip(evalvars, evalints))
        # Tokenize expression into operators, numbers, variables, parentheses
        tokens = re.findall(r'\(|\)|\+|\-|\*|\d+|\w+', expression)
        output = []   # stack for expressions
        operators = []    # stack for operators and parentheses

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

        # Operator precedence: '*' > '+'/'-'
        # When encountering operator token, pop while:
        # operators not empty and top not '(' and 
        # (token in (+,-) or top == '*')
        # means: if current is + or -, pop until '(' or empty or top is '('
        # if current is *, pop while top is '*', else push

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
                    # If token not in var_map, add variable term 1*token
                    if token not in var_map:
                        expr.add_term(Term(1, [token]))
                    else:
                        # token in var_map with coef == 1 => add constant 1 term
                        expr.add_term(Term(1, []))
                else:
                    # coef != 1 => add constant term coef
                    expr.add_term(Term(coef, []))
                output.append(expr)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator()
                operators.pop()  # Remove '('
            elif token in ['+', '-', '*']:
                while (operators and operators[-1] != '(' and
                      (token in ['+', '-'] or operators[-1] == '*')):
                    apply_operator()
                operators.append(token)
            i += 1

        while operators:
            apply_operator()

        simplified_terms = output[0].simplify()
        result_list = []
        for term in simplified_terms:
            if term.variables:
                term_string = str(term.coefficient) + "*" + "*".join(term.variables)
                result_list.append(term_string)
            else:
                result_list.append(str(term.coefficient))
        return result_list