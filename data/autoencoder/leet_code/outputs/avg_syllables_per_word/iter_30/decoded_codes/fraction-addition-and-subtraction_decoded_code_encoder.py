from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        g = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= g
        self.denominator //= g
        # Keep denominator positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Normalize expression by replacing "-" with "+-" and then split by "+"
        # This ensures all fractions are separated, including those with negative numerators
        parts = expression.replace("-", "+-").split("+")
        result = Fraction(0, 1)
        for frac_str in parts:
            if frac_str:
                numerator_str, denominator_str = frac_str.split("/")
                frac = Fraction(int(numerator_str), int(denominator_str))
                result = result + frac
        return f"{result.numerator}/{result.denominator}"