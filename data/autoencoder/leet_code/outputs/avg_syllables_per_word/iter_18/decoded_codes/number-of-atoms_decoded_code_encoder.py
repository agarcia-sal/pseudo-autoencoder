from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> dict:
            atom_count = defaultdict(int)
            # Pattern: uppercase letter followed by lowercase letters and optional digits
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element, count in elements:
                atom_count[element] += int(count) if count else 1
            return atom_count

        def multiply_counts(counts: dict, multiplier: int) -> dict:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        length = len(formula)

        while i < length:
            char = formula[i]
            if char == '(':
                stack.append(defaultdict(int))
                i += 1
            elif char == ')':
                i += 1
                j = i
                while j < length and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j]) if j > i else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j
            else:
                j = i + 1
                while j < length and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j

        final_count = stack.pop()
        result_parts = []
        for element in sorted(final_count):
            result_parts.append(element)
            if final_count[element] > 1:
                result_parts.append(str(final_count[element]))
        return ''.join(result_parts)