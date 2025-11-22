import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> dict:
            atom_count = defaultdict(int)
            # Find all occurrences of element symbols with optional count
            # Match an uppercase letter followed by lowercase letters, then optional digits
            pattern = r'([A-Z][a-z]*)(\d*)'
            elements = re.findall(pattern, segment)
            for element, count in elements:
                if count != '':
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
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                if j > i:
                    multiplier = int(formula[i:j])
                else:
                    multiplier = 1
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
        result_string = ''
        for element in sorted(final_count.keys()):
            count = final_count[element]
            if count > 1:
                result_string += element + str(count)
            else:
                result_string += element
        return result_string