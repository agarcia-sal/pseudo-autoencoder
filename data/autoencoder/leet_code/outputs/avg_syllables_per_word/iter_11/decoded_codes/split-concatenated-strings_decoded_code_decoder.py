from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            reversed_str = strs[i][::-1]
            if reversed_str > strs[i]:
                strs[i] = reversed_str

        doubled_strs = strs + strs
        max_string = ""

        n = len(strs)
        for i in range(n):
            for is_reversed in [False, True]:
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining = "".join(doubled_strs[i+1:i+n])
                for pos in range(len(current)):
                    candidate = current[pos:] + remaining + current[:pos]
                    if candidate > max_string:
                        max_string = candidate

        return max_string