ratios = [1, 1/9, 1/99, 1/999, 1/9999]

def valueOf(s):
    if '(' not in s:
        return float(s)
    li, ri, di = s.find('('), s.find(')'), s.find('.')
    intNR = float(s[:li])
    nr_len = li - di - 1
    rep = int(s[li+1:ri])
    rep_len = ri - li - 1
    return intNR + rep * 10**(-nr_len) * ratios[rep_len]

def isRationalEqual(s, t):
    return abs(valueOf(s) - valueOf(t)) < 1e-9