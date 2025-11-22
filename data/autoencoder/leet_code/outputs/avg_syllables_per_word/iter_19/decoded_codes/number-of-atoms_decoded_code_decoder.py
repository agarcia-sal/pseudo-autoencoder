import collections
import re

class Solution:
    def countOfAtoms(self, formula):
        def parse(segment):
            atom_count = collections.defaultdict(int)
            # Regex: one uppercase letter, zero or more lowercase letters, zero or more digits
            pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
            for element, count in pattern.findall(segment):
                if count == '':
                    atom_count[element] += 1
                else:
                    atom_count[element] += int(count)
            return atom_count

        def multiply_counts(counts, multiplier):
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
                segment_count = collections.defaultdict(int)
                j = i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                if j > i + 1:
                    multiplier = int(formula[i + 1:j])
                else:
                    multiplier = 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                for element in segment_count:
                    stack[-1][element] += segment_count[element]
                i = j

        final_count = stack.pop()
        result = []
        for element in sorted(final_count):
            result.append(element)
            count = final_count[element]
            if count > 1:
                result.append(str(count))
        return ''.join(result)