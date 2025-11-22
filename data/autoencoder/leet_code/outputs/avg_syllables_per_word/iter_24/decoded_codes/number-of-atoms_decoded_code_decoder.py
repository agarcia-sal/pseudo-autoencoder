import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        def parse(segment):
            atom_count = defaultdict(int)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            for elem, cnt in pattern.findall(segment):
                atom_count[elem] += int(cnt) if cnt else 1
            return atom_count

        def multiply_counts(counts, multiplier):
            for elem in counts:
                counts[elem] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i+1:j]) if j > i+1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for elem, cnt in segment_count.items():
                    stack[-1][elem] += cnt
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for elem, cnt in segment_count.items():
                    stack[-1][elem] += cnt
                i = j

        final_count = stack.pop()
        result = []
        for elem in sorted(final_count.keys()):
            result.append(elem)
            if final_count[elem] > 1:
                result.append(str(final_count[elem]))
        return ''.join(result)