from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> defaultdict[int]:
            atom_count = defaultdict(int)
            # Matches patterns like: Element symbols with optional digits, e.g. H2, Mg, O
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            elements = pattern.findall(segment)
            for element, count_str in elements:
                atom_count[element] += int(count_str) if count_str else 1
            return atom_count

        def multiply_counts(counts: defaultdict[int], multiplier: int) -> defaultdict[int]:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack: list[defaultdict[int]] = [defaultdict(int)]
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
                multiplier = int(formula[i+1:j]) if j > i + 1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                top = stack[-1]
                for element, count in segment_count.items():
                    top[element] += count
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                top = stack[-1]
                for element, count in segment_count.items():
                    top[element] += count
                i = j

        final_count = stack.pop()
        result = []
        for element in sorted(final_count.keys()):
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)