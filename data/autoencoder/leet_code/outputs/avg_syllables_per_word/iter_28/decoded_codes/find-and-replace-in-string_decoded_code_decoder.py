from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result = []
        prev_end = 0
        for idx, src, tgt in replacements:
            if idx > prev_end:
                result.append(s[prev_end:idx])
            elif idx < prev_end:
                # Overlapping replacement, skip or handle accordingly
                # According to problem spec, replacements don't overlap, but we handle gracefully
                continue
            end_idx = idx + len(src)
            if s[idx:end_idx] == src:
                result.append(tgt)
            else:
                result.append(s[idx:end_idx])
            prev_end = max(prev_end, end_idx)
        if prev_end < len(s):
            result.append(s[prev_end:])
        return ''.join(result)