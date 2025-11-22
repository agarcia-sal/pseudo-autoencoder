from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> defaultdict:
            atom_count = defaultdict(int)
            # Matches element symbols with optional counts: Capital letter + lowercase letters + digits (optional)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            for match in pattern.finditer(segment):
                element = match.group(1)
                count_str = match.group(2)
                count = int(count_str) if count_str else 1
                atom_count[element] += count
            return atom_count

        def multiply_counts(counts: defaultdict, multiplier: int) -> defaultdict:
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
                segment = formula[i:j]
                segment_count = parse(segment)
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j

        final_count = stack.pop()
        sorted_elements = sorted(final_count.keys())
        result_string = []
        for element in sorted_elements:
            result_string.append(element)
            count = final_count[element]
            if count > 1:
                result_string.append(str(count))
        return ''.join(result_string)