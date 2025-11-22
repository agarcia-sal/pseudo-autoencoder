class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1,
                  1/9,
                  1/99,
                  1/999,
                  1/9999]

        def valueOf(x: str) -> float:
            leftParenIndex = x.find('(')
            if leftParenIndex == -1:
                return float(x)

            rightParenIndex = x.find(')')
            dotIndex = x.find('.')

            # Convert the non-repeating part before the parentheses to float
            # The substring is from start to one before '('
            integer_and_non_repeating = float(x[:leftParenIndex])

            # Length of non-repeating decimal digits
            non_repeating_length = leftParenIndex - dotIndex - 1

            # Repeating part inside the parentheses as integer
            repeating = int(x[leftParenIndex + 1:rightParenIndex])

            # Length of repeating digits
            repeating_length = rightParenIndex - leftParenIndex - 1

            # Calculate the fractional value contributed by the repeating section
            # repeated fraction = repeating * (10^-non_repeating_length) * ratios[repeating_length]
            return integer_and_non_repeating + repeating * (10 ** (-non_repeating_length)) * ratios[repeating_length]

        return abs(valueOf(s) - valueOf(t)) < 1e-9