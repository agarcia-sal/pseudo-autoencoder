import math

def minAbbreviation(target, dictionary):
    inf = math.inf
    filtered = [w for w in dictionary if len(w) == len(target)]

    def is_valid(s, abbr):
        i, j = 0, 0
        while i < len(s) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                shift = 0
                while j < len(abbr) and abbr[j].isdigit():
                    shift = shift * 10 + int(abbr[j])
                    j += 1
                i += shift
            else:
                if s[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(s) and j == len(abbr)

    abbrs = set()
    def generate_abbrs(word, n, abbr="", i=0, skip=0):
        if i == n:
            if skip > 0:
                abbr += str(skip)
            abbrs.add(abbr)
            return
        generate_abbrs(word, n, abbr, i+1, skip+1)
        if skip > 0:
            abbr += str(skip)
        generate_abbrs(word, n, abbr + word[i], i+1, 0)

    def find_unique():
        for length in range(1, len(target)+1):
            abbrs.clear()
            generate_abbrs(target, len(target))
            min_abbr = None
            min_len = inf
            for abbr in abbrs:
                if len(abbr) == length:
                    if all(not is_valid(w, abbr) for w in filtered):
                        if len(abbr) < min_len:
                            min_len = len(abbr)
                            min_abbr = abbr
            if min_abbr is not None:
                return min_abbr
        return None

    return find_unique()