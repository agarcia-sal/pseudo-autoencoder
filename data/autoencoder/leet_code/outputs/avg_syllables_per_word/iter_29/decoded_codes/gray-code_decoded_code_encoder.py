class Solution:
    def grayCode(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        extended_list = [mask | num for num in reversed(prev_gray)]
        return prev_gray + extended_list