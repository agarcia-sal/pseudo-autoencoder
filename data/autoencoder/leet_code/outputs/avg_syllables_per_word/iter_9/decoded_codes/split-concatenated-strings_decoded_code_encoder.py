class Solution:
    def splitLoopedString(self, strs):
        n = len(strs)
        for i in range(n):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        doubled_strs = strs + strs
        max_string = ""
        concatenated = [''] * (2 * n)
        concatenated[:n] = strs
        concatenated[n:] = strs

        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                remaining = ''.join(doubled_strs[i+1:i+n])
                length = len(current)
                for j in range(length):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate
        return max_string