class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1,
                  1 / 9,
                  1 / 99,
                  1 / 999,
                  1 / 9999]

        def valueOf(s: str) -> float:
            leftParenIndex = s.find('(')
            if leftParenIndex == -1:
                # no repeating part
                return float(s)

            rightParenIndex = s.find(')')
            dotIndex = s.find('.')

            # substring s[0:leftParenIndex] excludes '('
            integerAndNonRepeating = float(s[:leftParenIndex])
            nonRepeatingLength = leftParenIndex - dotIndex - 1

            # repeating substring inside parentheses, convert to int
            repeating = int(s[leftParenIndex + 1:rightParenIndex])
            repeatingLength = rightParenIndex - leftParenIndex - 1

            return integerAndNonRepeating + repeating * pow(0.1, nonRepeatingLength) * ratios[repeatingLength]

        return abs(valueOf(s) - valueOf(t)) < 1e-9