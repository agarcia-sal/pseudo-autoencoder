from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            rev_str = strs[i][::-1]
            if rev_str > strs[i]:
                strs[i] = rev_str

        doubled_strs = strs + strs
        max_string = ""

        n = len(strs)
        for start_index in range(n):
            for is_reversed in (False, True):
                current = strs[start_index][::-1] if is_reversed else strs[start_index]
                remaining = "".join(doubled_strs[start_index+1:start_index+n])
                length = len(current)
                for cut_position in range(length):
                    candidate = current[cut_position:] + remaining + current[:cut_position]
                    if candidate > max_string:
                        max_string = candidate

        return max_string