from typing import List

class Solution:
    def findReplaceString(
        self, 
        s: str, 
        indices: List[int], 
        sources: List[str], 
        targets: List[str]
    ) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0
        for index, source, target in replacements:
            if index < prev_end:
                # Overlapping replacement, skip or treat depending on that logic; 
                # original pseudocode doesn't specify overlap policy.
                # We assume non-overlapping indices and skip to next iteration.
                continue

            result.append(s[prev_end:index])

            source_len = len(source)
            if s[index:index + source_len] == source:
                result.append(target)
                prev_end = index + source_len
            else:
                result.append(s[index:index + source_len])
                prev_end = index + source_len

        result.append(s[prev_end:])
        return ''.join(result)