from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Combine and sort replacements by indices
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])

        result = []
        prev_end = 0

        for index, source, target in replacements:
            # Append substring between previous end and current replacement start
            result.append(s[prev_end:index])
            # Check if source matches the substring in s at the current index
            if s[index:index + len(source)] == source:
                result.append(target)
                prev_end = index + len(source)
            else:
                # If no match, append the original substring and update prev_end accordingly
                result.append(s[index:index + len(source)])
                prev_end = index + len(source)

        # Append the remaining substring after the last replacement
        result.append(s[prev_end:])
        return ''.join(result)