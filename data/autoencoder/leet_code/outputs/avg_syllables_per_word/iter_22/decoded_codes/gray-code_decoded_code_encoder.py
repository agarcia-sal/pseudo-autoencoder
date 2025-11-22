class Solution:
    def grayCode(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        reversed_prev_gray = prev_gray[::-1]
        reflected_list = [mask | num for num in reversed_prev_gray]
        current_gray = prev_gray + reflected_list
        return current_gray