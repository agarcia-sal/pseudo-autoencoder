class Solution:
    def splitLoopedString(self, strs):
        # Step 1: Replace each string with its lexicographically max between itself and its reverse
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs
        max_string = ""
        n = len(strs)

        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining = "".join(doubled_strs[i+1:i+1+n])
                length = len(current)
                for j in range(length):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate

        return max_string