import re
from collections import defaultdict

def countOfAtoms(formula):
    def parse(segment):
        counts = defaultdict(int)
        for atom, num in re.findall(r'([A-Z][a-z]*)(\d*)', segment):
            counts[atom] += int(num or '1')
        return counts

    def mult(counts, m):
        for atom in counts:
            counts[atom] *= m
        return counts

    stack = [defaultdict(int)]
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            stack.append(defaultdict(int))
            i += 1
        elif formula[i] == ')':
            j = i + 1
            while j < len(formula) and formula[j].isdigit():
                j += 1
            m = int(formula[i+1:j]) if j > i + 1 else 1
            top = mult(stack.pop(), m)
            for atom, count in top.items():
                stack[-1][atom] += count
            i = j
        else:
            j = i + 1
            while j < len(formula) and (formula[j].islower() or formula[j].isdigit()):
                j += 1
            partial = parse(formula[i:j])
            for atom, count in partial.items():
                stack[-1][atom] += count
            i = j

    res = stack.pop()
    return ''.join(atom + (str(count) if count > 1 else '') for atom, count in sorted(res.items()))