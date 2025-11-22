import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(segment: str) -> collections.defaultdict[int]:
            atom_count = collections.defaultdict(int)
            # Matches element symbol and optional count
            elements = re.findall(r'([A-Z][a-z]*)(\d*)', segment)
            for element_name, count_string in elements:
                count_value = int(count_string) if count_string else 1
                atom_count[element_name] += count_value
            return atom_count

        def multiply_counts(counts: collections.defaultdict[int], multiplier: int) -> collections.defaultdict[int]:
            for element_name in counts:
                counts[element_name] *= multiplier
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
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j]) if j > i else 1
                segment_count = multiply_counts(stack.pop(), multiplier)
                top_counts = stack[-1]
                for element_name, count_value in segment_count.items():
                    top_counts[element_name] += count_value
                i = j
            else:
                j = i + 1
                while j < n and (formula[j].islower() or formula[j].isdigit()):
                    j += 1
                segment_count = parse(formula[i:j])
                top_counts = stack[-1]
                for element_name, count_value in segment_count.items():
                    top_counts[element_name] += count_value
                i = j

        final_count = stack.pop()
        result = []
        for element_name in sorted(final_count):
            count = final_count[element_name]
            if count == 1:
                result.append(element_name)
            else:
                result.append(element_name + str(count))
        return ''.join(result)