from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)
        # Step 1: For each string, replace it with its reversed form if reversed is lex greater
        for i in range(n):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs  # For circular concatenation
        max_string = ""

        for i in range(n):
            for is_reversed in (False, True):
                # current string at index i (reversed or not)
                current = strs[i][::-1] if is_reversed else strs[i]
                # remaining concatenation of all strings except current one
                # from i+1 to i+n-1 in doubled_strs (wrap around)
                remaining = "".join(doubled_strs[i+1:i+n])

                length_current = len(current)
                for cut_pos in range(length_current):
                    # candidate string by "cutting" current string at cut_pos
                    # concat suffix of current from cut_pos to end + remaining + prefix current from 0 to cut_pos
                    candidate = current[cut_pos:] + remaining + current[:cut_pos]
                    if candidate > max_string:
                        max_string = candidate
        return max_string