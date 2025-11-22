import math

def repeatedStringMatch(a, b):
    r = math.ceil(len(b) / len(a))
    if b in a * r:
        return r
    if b in a * (r + 1):
        return r + 1
    return -1