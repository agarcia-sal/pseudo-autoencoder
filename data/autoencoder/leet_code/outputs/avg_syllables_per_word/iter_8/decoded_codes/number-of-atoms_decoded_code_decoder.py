import re
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula):
        def parse(segment):
            atom_count = defaultdict(int)
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            matches = pattern.findall(segment)
            for element, count in matches:
                if count == '':
                    count_val = 1
                else:
                    count_val = int(count)
                atom_count[element] += count_val
            return atom_count

        def multiply_counts(counts, multiplier):
            for element in counts:
                counts[element] *= multiplier
            return counts

        stack = [defaultdict(int)]
        i = 0
        length = len(formula)
        while i < length:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                j = i + 1
                while j < length and formula[j].isdigit():
                    j += 1
                if j > i + 1:
                    multiplier = int(formula[i+1:j])
                else:
                    multiplier = 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j
            else:
                j = i + 1
                while j < length and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j
        final_count = stack.pop()
        result = []
        for element in sorted(final_count):
            count = final_count[element]
            if count > 1:
                result.append(f"{element}{count}")
            else:
                result.append(element)
        return "".join(result)