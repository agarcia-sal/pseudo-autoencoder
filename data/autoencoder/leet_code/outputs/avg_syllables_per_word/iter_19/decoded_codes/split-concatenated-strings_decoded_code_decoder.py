from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # Preprocess each string to its lexicographically maximum form between itself and reversed
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        # Prepare doubled list to simulate circular concatenation
        doubled_strs = strs + strs

        max_string = ""

        n = len(strs)
        # Iterate over all starting strings
        for i in range(n):
            for is_reversed in (False, True):
                curr = strs[i][::-1] if is_reversed else strs[i]
                # Concatenate all other strings in order
                remaining = ''.join(doubled_strs[i+1:i+n])
                length = len(curr)
                # Try all cutting positions
                for cut in range(length):
                    candidate = curr[cut:] + remaining + curr[:cut]
                    if candidate > max_string:
                        max_string = candidate
        return max_string