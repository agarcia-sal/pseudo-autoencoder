import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> collections.defaultdict:
            atom_count = collections.defaultdict(int)
            # Regex to match element symbols and counts: element starting with uppercase letter followed by lowercase letters, then digits (optional)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            for element, count in pattern.findall(segment):
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
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i + 1:j]) if j > i + 1 else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, cnt in segment_count.items():
                    stack[-1][element] += cnt
                i = j
            else:
                j = i + 1
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