class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        # To efficiently build strings use list then join
        row_chars = [[] for _ in range(numRows)]
        for c in s:
            row_chars[current_row].append(c)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return ''.join(''.join(rc) for rc in row_chars)