from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs
        max_string = ""
        n = len(strs)

        for i in range(n):
            for reversed_flag in (False, True):
                current = strs[i][::-1] if reversed_flag else strs[i]
                remaining = "".join(doubled_strs[i + 1:i + n])
                length = len(current)

                for cut in range(length):
                    candidate = current[cut:] + remaining + current[:cut]
                    if candidate > max_string:
                        max_string = candidate
        return max_string