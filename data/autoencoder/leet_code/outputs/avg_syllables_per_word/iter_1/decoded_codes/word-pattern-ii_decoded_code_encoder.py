def wordPatternMatch(pattern, s):
    def backtrack(pIdx, sIdx, mapping, used):
        if pIdx == len(pattern) and sIdx == len(s):
            return True
        if pIdx == len(pattern) or sIdx == len(s):
            return False

        c = pattern[pIdx]
        if c in mapping:
            w = mapping[c]
            if s[sIdx:sIdx+len(w)] != w:
                return False
            return backtrack(pIdx + 1, sIdx + len(w), mapping, used)

        for end in range(sIdx + 1, len(s) + 1):
            w = s[sIdx:end]
            if w in used:
                continue
            mapping[c], used = w, used | {w}
            if backtrack(pIdx + 1, end, mapping, used):
                return True
            del mapping[c]
            used = used - {w}
        return False

    return backtrack(0, 0, {}, set())