from typing import List

class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        n = len(strs)
        # Step 1: replace each string with its lexicographically maximum between itself and its reverse
        for i in range(n):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs
        max_string = ""

        for i in range(n):
            for is_reversed in [False, True]:
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining_start = i + 1
                remaining_end = i + n
                remaining = "".join(doubled_strs[remaining_start:remaining_end])

                length_current = len(current)
                for j in range(length_current):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate

        return max_string