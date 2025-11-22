from fractions import Fraction

def simplify_expression(expr):
    expr = expr.replace('-', '+-')
    parts = expr.split('+')
    result = sum(Fraction(f) for f in parts if f)
    return f"{result.numerator}/{result.denominator}"