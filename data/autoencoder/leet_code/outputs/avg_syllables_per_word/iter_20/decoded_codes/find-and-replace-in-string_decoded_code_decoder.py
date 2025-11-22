from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0
        for index, source, target in replacements:
            if index > len(s):
                # If index is out of bounds, append previous substring and skip
                continue
            result.append(s[prev_end:index])
            end_index = index + len(source)
            if end_index <= len(s) and s[index:end_index] == source:
                result.append(target)
                prev_end = end_index
            else:
                result.append(s[index:end_index])
                prev_end = end_index
        result.append(s[prev_end:])
        return ''.join(result)