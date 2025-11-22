import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> collections.defaultdict:
            atom_count = collections.defaultdict(int)
            # Matches patterns: Element starting with uppercase, optional lowercase letters, optional digits
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element, count in elements:
                atom_count[element] += int(count) if count else 1
            return atom_count

        def multiply_counts(counts: collections.defaultdict, multiplier: int) -> collections.defaultdict:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)
        while i < n:
            char = formula[i]
            if char == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif char == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i+1:j]) if j > i+1 else 1
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
        for element in sorted(final_count.keys()):
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)