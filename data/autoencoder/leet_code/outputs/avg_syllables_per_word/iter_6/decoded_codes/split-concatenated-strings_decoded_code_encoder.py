class Solution:
    def splitLoopedString(self, strs):
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled = strs + strs
        max_string = ""
        n = len(strs)

        for i in range(n):
            for rev_flag in [False, True]:
                cur = strs[i][::-1] if rev_flag else strs[i]
                remaining = "".join(doubled[i+1:i+n])
                for cut in range(len(cur)+1):
                    candidate = cur[cut:] + remaining + cur[:cut]
                    if candidate > max_string:
                        max_string = candidate
        return max_string