class Solution:
    def grayCode(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        reversed_prev_gray = prev_gray[::-1]
        extended_list = []
        for num in reversed_prev_gray:
            combined_num = mask | num
            extended_list.append(combined_num)
        current_gray = prev_gray + extended_list
        return current_gray