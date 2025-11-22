class Solution:
    def splitLoopedString(self, strs):
        # Step 1: maximize each string by checking its reverse
        for i in range(len(strs)):
            reversed_string = strs[i][::-1]
            if reversed_string > strs[i]:
                strs[i] = reversed_string

        # Step 2: concatenate strs with itself to handle circular concatenation
        doubled_strs = strs + strs

        max_string = ""
        n = len(strs)
        for i in range(n):
            for is_reversed in (False, True):
                current = strs[i][::-1] if is_reversed else strs[i]
                # Join from i+1 to i+n-1 from doubled_strs
                remaining = "".join(doubled_strs[i+1:i+n])
                length = len(current)
                for cut in range(length + 1):
                    candidate = current[cut:] + remaining + current[:cut]
                    if candidate > max_string:
                        max_string = candidate

        return max_string