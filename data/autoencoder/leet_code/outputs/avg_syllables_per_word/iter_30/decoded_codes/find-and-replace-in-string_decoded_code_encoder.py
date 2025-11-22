from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append unchanged substring before the current replacement index
            if index > prev_end:
                result.append(s[prev_end:index])

            source_len = len(source)
            # Check if the source substring matches
            if s[index:index + source_len] == source:
                result.append(target)
                prev_end = index + source_len
            else:
                # If no match, append the original substring as is
                result.append(s[index:index + source_len])
                prev_end = index + source_len

        # Append the remaining substring after the last replacement
        if prev_end < len(s):
            result.append(s[prev_end:])

        return "".join(result)