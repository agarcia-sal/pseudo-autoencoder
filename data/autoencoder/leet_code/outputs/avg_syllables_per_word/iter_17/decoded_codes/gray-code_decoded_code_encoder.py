class Solution:
    def grayCode(self, number_n: int) -> list[int]:
        if number_n == 0:
            return [0]
        previous_gray_codes = self.grayCode(number_n - 1)
        bit_mask = 1 << (number_n - 1)
        reflected_list = [bit_mask | number for number in reversed(previous_gray_codes)]
        current_gray_codes = previous_gray_codes + reflected_list
        return current_gray_codes