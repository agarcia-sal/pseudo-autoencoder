from typing import List, Tuple

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Sort replacements by indices ascending
        replacements: List[Tuple[int, str, str]] = sorted(
            zip(indices, sources, targets),
            key=lambda x: x[0]
        )

        result = []
        prev_end = 0
        for index, source, target in replacements:
            # Append substring from prev_end up to index (not inclusive)
            if prev_end < index:
                result.append(s[prev_end:index])
            # Check if substring of s starting at index matches source
            if s.startswith(source, index):
                result.append(target)
                prev_end = index + len(source)
            else:
                # If no match, append the original substring untouched
                result.append(s[index:index+len(source)])
                prev_end = index + len(source)
        # Append the remaining part of s after last replacement
        if prev_end < len(s):
            result.append(s[prev_end:])
        return ''.join(result)