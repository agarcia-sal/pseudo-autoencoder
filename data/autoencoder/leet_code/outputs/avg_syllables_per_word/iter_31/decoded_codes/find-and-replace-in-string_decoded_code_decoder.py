from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0
        for index, source, target in replacements:
            # Append substring between previous replacement and current index
            if index > prev_end:
                result.append(s[prev_end:index])
            elif index < prev_end:
                # overlapping or out-of-order replacements cause current index to be before prev_end
                # skip processing to avoid duplicate substrings
                continue
            # Check if the source matches the substring starting at index
            if s.startswith(source, index):
                result.append(target)
                prev_end = index + len(source)
            else:
                result.append(s[index:index + len(source)])
                prev_end = index + len(source)
        # Append any remaining substring after last replacement
        if prev_end < len(s):
            result.append(s[prev_end:])
        return "".join(result)