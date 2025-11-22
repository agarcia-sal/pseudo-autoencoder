class Solution:
    def rotatedDigits(self, n: int) -> int:
        change_digits = self.GetChangeDigits()
        same_digits = self.GetSameDigits()

        def is_good_number(num: int) -> bool:
            num_str = self.ConvertNumberToString(num)
            if all(d in change_digits or d in same_digits for d in num_str):
                if any(d in change_digits for d in num_str):
                    return True
            return False

        good_count = 0
        for i in range(1, n + 1):
            if is_good_number(i):
                good_count += 1

        return good_count

    def GetChangeDigits(self) -> set:
        # Digits that change to a different valid digit after rotation: 2->5, 5->2, 6->9, 9->6
        return {'2', '5', '6', '9'}

    def GetSameDigits(self) -> set:
        # Digits that remain the same after rotation: 0, 1, 8
        return {'0', '1', '8'}

    def ConvertNumberToString(self, num: int) -> str:
        return str(num)