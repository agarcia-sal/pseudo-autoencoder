from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)

        # Replace each string with its lexicographically maximum between original and reversed
        for i in range(n):
            reversed_str = strs[i][::-1]
            if reversed_str > strs[i]:
                strs[i] = reversed_str

        doubled_strs = strs + strs
        max_string = ""

        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                # Concatenate from i+1 to i+n-1 (modular via doubled_strs)
                remaining = "".join(doubled_strs[i+1:i+n])

                length_current = len(current)
                for j in range(length_current):
                    # candidate = current[j:] + remaining + current[:j]
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate

        return max_string