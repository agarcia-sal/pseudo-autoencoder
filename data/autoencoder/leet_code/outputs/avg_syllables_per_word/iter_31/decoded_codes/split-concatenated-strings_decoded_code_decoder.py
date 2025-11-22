from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # Step 1: For each string in strs, replace it with its lexicographically
        # maximum between itself and its reversed form.
        for i in range(len(strs)):
            reversed_string = strs[i][::-1]
            if reversed_string > strs[i]:
                strs[i] = reversed_string

        # Double the list to simulate circular rotation easily
        doubled_strs = strs + strs

        max_string = ""

        n = len(strs)

        # Iterate over each starting index
        for i in range(n):
            # For each string, try both the original and reversed form as the starting point
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]

                # Remaining strings after current (n-1 strings)
                remaining = "".join(doubled_strs[i + 1 : i + n])

                length_current = len(current)
                # Try every possible cut position in current
                for cut_pos in range(length_current):
                    # Construct candidate string with rotated current string
                    candidate = (
                        current[cut_pos:] + remaining + current[:cut_pos]
                    )
                    if candidate > max_string:
                        max_string = candidate

        return max_string