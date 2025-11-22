def remove_comments(source):
    in_block = False
    result = []
    curr = []

    for line in source:
        i = 0
        while i < len(line):
            if in_block:
                if line[i:i+2] == "*/":
                    in_block = False
                    i += 1
            else:
                if line[i:i+2] == "//":
                    break
                elif line[i:i+2] == "/*":
                    in_block = True
                    i += 1
                else:
                    curr.append(line[i])
            i += 1
        if curr and not in_block:
            result.append("".join(curr))
            curr = []

    return result