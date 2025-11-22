def restoreIpAddresses(s):
    def is_valid(seg):
        return len(seg) == 1 or (seg[0] != '0' and int(seg) <= 255)

    def backtrack(i, path):
        if len(path) == 4:
            if i == len(s):
                result.append(".".join(path))
            return
        for l in range(1, 4):
            if i + l <= len(s):
                seg = s[i:i+l]
                if is_valid(seg):
                    backtrack(i + l, path + [seg])

    result = []
    backtrack(0, [])
    return result