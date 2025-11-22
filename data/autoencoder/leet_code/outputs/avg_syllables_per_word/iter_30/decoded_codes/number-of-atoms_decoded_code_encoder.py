import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> collections.defaultdict:
            atom_count = collections.defaultdict(int)
            # Regex to find all occurrences of element names followed by optional counts
            # Element: uppercase letter + zero or more lowercase letters
            # Count: zero or more digits (possibly empty)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            for element, count in pattern.findall(segment):
                if count == '':
                    atom_count[element] += 1
                else:
                    atom_count[element] += int(count)
            return atom_count

        def multiply_counts(counts: collections.defaultdict, multiplier: int) -> collections.defaultdict:
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)
        while i < n:
            c = formula[i]
            if c == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif c == ')':
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
            result.append(element)
            if final_count[element] > 1:
                result.append(str(final_count[element]))
        return ''.join(result)