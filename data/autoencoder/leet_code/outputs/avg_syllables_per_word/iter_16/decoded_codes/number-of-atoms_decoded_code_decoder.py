import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> collections.defaultdict:
            atom_count = collections.defaultdict(int)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            elements = pattern.findall(segment)
            for elem, cnt_str in elements:
                atom_count[elem] += int(cnt_str) if cnt_str else 1
            return atom_count

        def multiply_counts(counts: collections.defaultdict, multiplier: int) -> collections.defaultdict:
            for elem in counts:
                counts[elem] *= multiplier
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
                multiplier = int(formula[i+1:j]) if j > i + 1 else 1
                top_counts = multiply_counts(stack.pop(), multiplier)
                for elem, cnt in top_counts.items():
                    stack[-1][elem] += cnt
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment = formula[i:j]
                segment_count = parse(segment)
                for elem, cnt in segment_count.items():
                    stack[-1][elem] += cnt
                i = j

        final_count = stack.pop()
        result_parts = []
        for elem in sorted(final_count):
            result_parts.append(elem)
            if final_count[elem] > 1:
                result_parts.append(str(final_count[elem]))
        return ''.join(result_parts)