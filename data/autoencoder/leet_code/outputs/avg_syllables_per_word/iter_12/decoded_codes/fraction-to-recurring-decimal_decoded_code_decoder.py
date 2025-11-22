class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Determine the sign of the result
        if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
            sign = "-"
        else:
            sign = ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        remainder = numerator - quotient * denominator
        integer_part = str(quotient)

        if remainder == 0:
            return sign + integer_part

        seen_remainders = {}
        fractional_part = []

        while remainder != 0:
            if remainder in seen_remainders:
                start = seen_remainders[remainder]
                non_repeating = "".join(fractional_part[:start])
                repeating = "".join(fractional_part[start:])
                return f"{sign}{integer_part}.{non_repeating}({repeating})"

            seen_remainders[remainder] = len(fractional_part)

            remainder *= 10
            quotient = remainder // denominator
            remainder = remainder - quotient * denominator

            fractional_part.append(str(quotient))

        return sign + integer_part + "." + "".join(fractional_part)