from typing import Dict

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Determine the sign
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        integer_part = str(quotient)

        if remainder == 0:
            return sign + integer_part

        seen_remainders: Dict[int, int] = {}
        fractional_part = []

        while remainder != 0:
            if remainder in seen_remainders:
                start = seen_remainders[remainder]
                non_repeating = "".join(fractional_part[:start])
                repeating = "".join(fractional_part[start:])
                return sign + integer_part + "." + non_repeating + "(" + repeating + ")"

            seen_remainders[remainder] = len(fractional_part)
            remainder *= 10
            quotient, remainder = divmod(remainder, denominator)
            fractional_part.append(str(quotient))

        return sign + integer_part + "." + "".join(fractional_part)