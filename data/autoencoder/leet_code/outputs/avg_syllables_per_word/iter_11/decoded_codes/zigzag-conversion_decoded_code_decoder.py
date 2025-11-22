class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        rows = ['' for _ in range(numRows)]

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        result = ''.join(rows)
        return result