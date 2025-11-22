class Solution:
    def convert(self, string_s: str, integer_numRows: int) -> str:
        if integer_numRows == 1:
            return string_s

        list_rows = [''] * integer_numRows
        integer_current_row = 0
        boolean_going_down = False

        list_rows = ['' for _ in range(integer_numRows)]

        for character in string_s:
            list_rows[integer_current_row] += character
            if integer_current_row == 0 or integer_current_row == integer_numRows - 1:
                boolean_going_down = not boolean_going_down
            if boolean_going_down:
                integer_current_row += 1
            else:
                integer_current_row -= 1

        string_result = self.JoinStrings(list_rows)
        return string_result

    def JoinStrings(self, list_of_strings: list[str]) -> str:
        return ''.join(list_of_strings)