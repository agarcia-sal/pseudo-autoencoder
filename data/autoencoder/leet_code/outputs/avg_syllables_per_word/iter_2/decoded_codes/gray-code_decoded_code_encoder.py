class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        prev_gray = self.grayCode(n - 1)
        mask = 1 << (n - 1)
        reflected_list = reversed(prev_gray)
        reflected_with_mask = []
        for num in reflected_list:
            reflected_with_mask.append(mask | num)
        current_gray = prev_gray + reflected_with_mask
        return current_gray