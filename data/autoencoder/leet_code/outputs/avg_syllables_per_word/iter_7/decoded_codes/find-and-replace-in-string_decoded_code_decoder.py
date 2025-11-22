from typing import List, Tuple

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements: List[Tuple[int, str, str]] = sorted(zip(indices, sources, targets), key=lambda x: x[0])
        result: List[str] = []
        prev_end = 0
        for index, source, target in replacements:
            result.append(s[prev_end:index])
            if s[index:index+len(source)] == source:
                result.append(target)
            else:
                result.append(s[index:index+len(source)])
            prev_end = index + len(source)
        result.append(s[prev_end:])
        return "".join(result)