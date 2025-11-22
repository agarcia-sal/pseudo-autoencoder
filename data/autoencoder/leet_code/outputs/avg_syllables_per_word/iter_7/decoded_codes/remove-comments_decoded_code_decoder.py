from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block_comment = False
        result: List[str] = []
        current_line: List[str] = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1
                else:
                    if line[i:i+2] == "//":
                        break
                    elif line[i:i+2] == "/*":
                        in_block_comment = True
                        i += 1
                    else:
                        current_line.append(line[i])
                i += 1
            if current_line and not in_block_comment:
                result.append("".join(current_line))
                current_line = []
        return result