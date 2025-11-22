class Solution:
    def splitLoopedString(self, strs):
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled = strs + strs
        max_str = ""

        n = len(strs)
        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining = "".join(doubled[i+1:i+n])
                for j in range(len(current)):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_str:
                        max_str = candidate

        return max_str