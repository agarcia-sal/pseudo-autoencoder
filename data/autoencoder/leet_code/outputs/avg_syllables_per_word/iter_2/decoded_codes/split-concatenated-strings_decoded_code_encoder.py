class Solution:
    def splitLoopedString(self, strs):
        for i in range(len(strs)):
            reversed_str = strs[i][::-1]
            if reversed_str > strs[i]:
                strs[i] = reversed_str

        doubled_strs = strs + strs
        max_string = ""
        n = len(strs)

        for i in range(n):
            for is_reversed in [False, True]:
                if is_reversed:
                    current = strs[i][::-1]
                else:
                    current = strs[i]
                remaining = "".join(doubled_strs[i+1:i+n])
                length = len(current)
                for j in range(length):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate
        return max_string