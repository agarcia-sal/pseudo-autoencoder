from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a list of tuples and sort by index
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])

        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append substring from prev_end up to but not including current index
            if prev_end < index:
                result.append(s[prev_end:index])
            # Check if source matches substring at s[index:index+len(source)]
            if s[index:index+len(source)] == source:
                result.append(target)
                prev_end = index + len(source)
            else:
                # Source doesn't match, append the original substring unchanged
                result.append(s[index:index+len(source)])
                prev_end = index + len(source)

        # Append remaining substring after last replacement
        if prev_end < len(s):
            result.append(s[prev_end:])

        return ''.join(result)