class Solution:
    def removeComments(self, source):
        in_block_comment = False
        result = []
        current_line = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block_comment:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block_comment = False
                        i += 1
                else:
                    if i + 1 < len(line):
                        if line[i:i+2] == "//":
                            break
                        elif line[i:i+2] == "/*":
                            in_block_comment = True
                            i += 1
                        else:
                            current_line.append(line[i])
                    else:
                        current_line.append(line[i])
                i += 1

            if current_line and not in_block_comment:
                result.append("".join(current_line))
                current_line = []

        return result