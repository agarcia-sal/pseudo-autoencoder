class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [
            1,
            1 / 9,
            1 / 99,
            1 / 999,
            1 / 9999,
            1 / 99999,
            1 / 999999,
            1 / 9999999,
            1 / 99999999,
            1 / 999999999
        ]

        def valueOf(x: str) -> float:
            leftParenIndex = x.find('(')
            if leftParenIndex == -1:
                # No repeating decimal part
                return float(x)

            rightParenIndex = x.find(')')
            dotIndex = x.find('.')

            # substring before '(' includes integer part and non-repeating decimal part
            integerAndNonRepeating = float(x[:leftParenIndex])

            nonRepeatingLength = leftParenIndex - dotIndex - 1  # digits after decimal before '('

            repeatingStr = x[leftParenIndex + 1:rightParenIndex]
            repeatingLength = rightParenIndex - leftParenIndex - 1

            repeating = int(repeatingStr) if repeatingStr else 0

            # valueOf = integerAndNonRepeating + repeating * 10^-nonRepeatingLength * ratios[repeatingLength]
            # ratios indexed by repeatingLength (max 9 here)
            if repeatingLength >= len(ratios):
                # compute ratio for larger repeating lengths
                ratio = 1 / (10 ** repeatingLength - 1)
            else:
                ratio = ratios[repeatingLength]

            return integerAndNonRepeating + repeating * pow(10, -nonRepeatingLength) * ratio

        return abs(valueOf(s) - valueOf(t)) < 1e-9