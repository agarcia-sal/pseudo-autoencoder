import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> dict[str, int]:
            atom_count = defaultdict(int)
            # Regex to find elements with optional counts, e.g., H2, He3, O
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element, count_str in elements:
                count = int(count_str) if count_str else 1
                atom_count[element] += count
            return atom_count

        def multiply_counts(counts: dict[str, int], multiplier: int) -> dict[str, int]:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            current_char = formula[i]
            if current_char == '(':
                stack.append(defaultdict(int))
                i += 1
            elif current_char == ')':
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i+1:j]) if j > i + 1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, cnt in segment_count.items():
                    stack[-1][element] += cnt
                i = j
            else:
                j = i + 1
                while j < len(formula) and (formula[j].islower() or formula[j].isdigit()):
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