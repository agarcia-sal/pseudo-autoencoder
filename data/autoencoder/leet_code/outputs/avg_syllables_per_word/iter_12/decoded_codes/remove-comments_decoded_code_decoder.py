from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        result = []
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1  # Skip the '/' of the closing block comment
                else:
                    if i + 1 < len(line) and line[i:i+2] == "//":
                        break  # Ignore the rest of the line
                    elif i + 1 < len(line) and line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1  # Skip the '*' of the opening block comment
                    else:
                        current_line.append(line[i])
                i += 1

            if not in_block_comment and current_line:
                result.append("".join(current_line))
                current_line = []

        return result