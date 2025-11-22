from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> defaultdict:
            atom_count = defaultdict(int)
            # Regex to match elements with optional count: element name starting with uppercase, followed by lowercase letters, and optional digits
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element, count in elements:
                if count:
                    atom_count[element] += int(count)
                else:
                    atom_count[element] += 1
            return atom_count

        def multiply_counts(counts: defaultdict, multiplier: int) -> defaultdict:
            for element in counts:
                counts[element] *= multiplier
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
                multiplier = int(formula[i+1:j]) if j > i + 1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j

        final_count = stack.pop()
        result = []
        for element in sorted(final_count):
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)