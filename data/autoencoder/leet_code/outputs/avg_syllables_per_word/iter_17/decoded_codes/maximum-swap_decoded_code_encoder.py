class Solution:
    def maximumSwap(self, number: int) -> int:
        digits = self.ConvertNumberToListOfDigits(number)
        last_occurrence = self.MapDigitToLastPosition(digits)

        for i, digit in enumerate(digits):
            for digit_candidate in range(9, digit, -1):
                if last_occurrence.get(digit_candidate, -1) > i:
                    j = last_occurrence[digit_candidate]
                    digits[i], digits[j] = digits[j], digits[i]
                    return self.ConvertListOfDigitsToNumber(digits)
        return number

    def ConvertNumberToListOfDigits(self, number: int) -> list[int]:
        # Convert number to list of its digits
        return [int(d) for d in str(number)]

    def MapDigitToLastPosition(self, digits: list[int]) -> dict[int, int]:
        # Map each digit to its last position in the digits list
        last_occ = {}
        for i, d in enumerate(digits):
            last_occ[d] = i
        return last_occ

    def ConvertListOfDigitsToNumber(self, digits: list[int]) -> int:
        # Convert list of digits back to the integer number
        return int(''.join(map(str, digits)))