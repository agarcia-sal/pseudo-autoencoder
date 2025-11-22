class Solution:
    def splitLoopedString(self, strs):
        # Optimize each string by replacing it with the lexicographically greater between itself and its reverse
        for i in range(len(strs)):
            reversed_str = strs[i][::-1]
            if reversed_str > strs[i]:
                strs[i] = reversed_str

        doubled_strs = strs + strs
        max_string = ""

        n = len(strs)
        for i in range(n):
            for is_reversed in [False, True]:
                current = strs[i][::-1] if is_reversed else strs[i]
                # Concatenate next n-1 strings from doubled_strs after index i
                remaining = "".join(doubled_strs[i+1:i+n])
                length = len(current)
                # Try all splits of current
                for j in range(length):
                    candidate = current[j:] + remaining + current[:j]
                    if candidate > max_string:
                        max_string = candidate

        return max_string