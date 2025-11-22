from math import inf
from itertools import permutations

def largestVariance(s):
    maxV = 0
    chars = set(s)

    def calcVar(sub, a, b):
        maxV = 0
        cntA = 0
        cntB = 0
        hasB = False
        firstB = False
        for c in sub:
            if c == a:
                cntA += 1
            if c == b:
                cntB += 1
                hasB = True
            if cntB > 0:
                maxV = max(maxV, cntA - cntB)
            elif cntB == 0 and firstB:
                maxV = max(maxV, cntA - 1)
            if cntB > cntA:
                cntA = 0
                cntB = 0
                firstB = hasB
        return maxV

    for a, b in permutations(chars, 2):
        if a != b:
            maxV = max(maxV, calcVar(s, a, b))

    return maxV