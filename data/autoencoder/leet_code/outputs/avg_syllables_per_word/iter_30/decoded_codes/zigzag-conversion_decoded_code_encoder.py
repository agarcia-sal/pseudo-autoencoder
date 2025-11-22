class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        res = []
        for char in s:
            # using list for efficient concatenation, will join later
            if not res:
                res = [''] * numRows
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(rows)