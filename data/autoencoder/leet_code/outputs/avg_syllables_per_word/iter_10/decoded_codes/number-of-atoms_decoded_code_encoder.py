import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment):
            atom_count = defaultdict(int)
            pattern = r'([A-Z][a-z]*)(\d*)'
            for element, count in re.findall(pattern, segment):
                atom_count[element] += int(count) if count else 1
            return atom_count

        def multiply_counts(counts, multiplier):
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            char = formula[i]
            if char == '(':
                stack.append(defaultdict(int))
                i += 1
            elif char == ')':
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j]) if j > i else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j

        final_count = stack.pop()
        result = []
        for element in sorted(final_count):
            count = final_count[element]
            result.append(element + (str(count) if count > 1 else ''))
        return ''.join(result)