class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        current_row = 0
        going_down = False
        result_rows = [''] * numRows  # To avoid string concatenation in place, better to build lists

        # Actually, building strings using += in Python is inefficient.
        # Using lists for each row is more efficient

        rows = [[] for _ in range(numRows)]
        current_row = 0
        going_down = False

        for c in s:
            rows[current_row].append(c)
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(''.join(row) for row in rows)