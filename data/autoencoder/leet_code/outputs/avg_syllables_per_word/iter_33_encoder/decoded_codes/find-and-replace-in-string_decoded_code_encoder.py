from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a list of tuples (index, source, target), sorted by index
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])

        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append substring from prev_end to current index
            result.append(s[prev_end:index])

            # Check if the substring at s[index:index+len(source)] matches source
            if s[index:index+len(source)] == source:
                result.append(target)
                prev_end = index + len(source)
            else:
                # If no match, append the original substring unchanged
                result.append(s[index:index+len(source)])
                prev_end = index + len(source)

        # Append the remainder of the string after the last replacement
        result.append(s[prev_end:])

        return ''.join(result)