class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = self.create_empty_string_list(numRows)
        current_row = 0
        going_down = False
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1
        return self.join_strings_in_list(rows)

    def create_empty_string_list(self, numRows: int) -> list:
        result = []
        for _ in range(numRows):
            result.append("")
        return result

    def join_strings_in_list(self, string_list: list) -> str:
        joined_string = ""
        for item in string_list:
            joined_string += item
        return joined_string