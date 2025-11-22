class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Determine the sign
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''

        # Use absolute values for the calculation
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        quotient, remainder = divmod(numerator, denominator)
        integer_part = str(quotient)

        # If no remainder, return just the integer part with sign
        if remainder == 0:
            return sign + integer_part

        seen_remainders = {}
        fractional_part = []

        while remainder != 0:
            if remainder in seen_remainders:
                start = seen_remainders[remainder]
                non_repeating = ''.join(fractional_part[:start])
                repeating = ''.join(fractional_part[start:])
                return sign + integer_part + '.' + non_repeating + '(' + repeating + ')'

            seen_remainders[remainder] = len(fractional_part)

            remainder *= 10
            quotient, remainder = divmod(remainder, denominator)
            fractional_part.append(str(quotient))

        return sign + integer_part + '.' + ''.join(fractional_part)