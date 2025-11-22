import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> dict:
            atom_count = defaultdict(int)
            # Find all occurrences of elements and their counts in the segment
            # An element is uppercase letter followed by zero or more lowercase letters
            # followed by zero or more digits
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            elements = pattern.findall(segment)
            for element, count in elements:
                if count:
                    atom_count[element] += int(count)
                else:
                    atom_count[element] += 1
            return atom_count

        def multiply_counts(counts: dict, multiplier: int) -> dict:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        while i < n:
            ch = formula[i]
            if ch == '(':
                stack.append(defaultdict(int))
                i += 1
            elif ch == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i+1:j]) if j > i+1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, cnt in segment_count.items():
                    stack[-1][element] += cnt
                i = j
            else:
                j = i + 1
                # element name can have lowercase letters
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element, cnt in segment_count.items():
                    stack[-1][element] += cnt
                i = j

        final_count = stack.pop()
        result = []
        for element in sorted(final_count.keys()):
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)