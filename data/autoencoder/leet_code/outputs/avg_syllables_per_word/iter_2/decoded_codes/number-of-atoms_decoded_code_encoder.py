from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment):
            atom_count = defaultdict(int)
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element, count in elements:
                if count:
                    atom_count[element] += int(count)
                else:
                    atom_count[element] += 1
            return atom_count

        def multiply_counts(counts, multiplier):
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    j += 1
                if j > i + 1:
                    multiplier = int(formula[i+1:j])
                else:
                    multiplier = 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j
            else:
                j = i + 1
                while j < len(formula) and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element, count in segment_count.items():
                    stack[-1][element] += count
                i = j

        final_count = stack.pop()
        result = ""
        for element in sorted(final_count.keys()):
            result += element
            if final_count[element] > 1:
                result += str(final_count[element])
        return result