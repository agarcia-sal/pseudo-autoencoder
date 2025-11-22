class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]

        prev_gray = self.grayCode(n - 1)

        mask = 1 << (n - 1)
        reflected_list = prev_gray[::-1]
        appended_list = []
        for num in reflected_list:
            appended_list.append(mask | num)

        current_gray = prev_gray + appended_list

        return current_gray