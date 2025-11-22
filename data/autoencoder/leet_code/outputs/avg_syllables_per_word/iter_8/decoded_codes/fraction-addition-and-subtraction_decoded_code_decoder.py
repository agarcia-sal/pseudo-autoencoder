from fractions import Fraction

class Solution:
    def fractionAddition(self, expression):
        fractions = expression.replace('-', '+-').split('+')
        result = sum(Fraction(f) for f in fractions if f)
        return str(result.numerator) + '/' + str(result.denominator)