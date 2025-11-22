from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append substring before current replacement
            result.append(s[prev_end:index])
            # Check if source matches the substring at the index
            if s[index:index + len(source)] == source:
                result.append(target)
                prev_end = index + len(source)
            else:
                # Source does not match; keep original substring
                result.append(s[index:index + len(source)])
                prev_end = index + len(source)

        # Append the remainder of the string after the last replacement
        result.append(s[prev_end:])

        return ''.join(result)