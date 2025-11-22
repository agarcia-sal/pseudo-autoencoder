from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)
        # For each string, replace it with its lexicographically maximum between itself and its reverse
        for i in range(n):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs
        max_string = ""

        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining = "".join(doubled_strs[i+1:i+n])
                length = len(current)

                for cut_pos in range(length + 1):
                    # Construct candidate string as current[cut_pos:] + remaining + current[:cut_pos]
                    candidate = current[cut_pos:] + remaining + current[:cut_pos]
                    if candidate > max_string:
                        max_string = candidate

        return max_string