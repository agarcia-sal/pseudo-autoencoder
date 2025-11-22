class Solution:
    def splitLoopedString(self, strs):
        # Step 1: Maximize each string by possibly reversing it if reversed > original
        for i in range(len(strs)):
            reversed_str = strs[i][::-1]
            if reversed_str > strs[i]:
                strs[i] = reversed_str

        doubled_strs = strs + strs
        max_string = ''

        for i in range(len(strs)):
            for is_reversed in (False, True):
                if is_reversed:
                    current = strs[i][::-1]
                else:
                    current = strs[i]

                remaining = ''.join(doubled_strs[i + 1:i + len(strs)])

                length = len(current)
                for cut_position in range(length):
                    # current[cut_position:] + remaining + current[:cut_position]
                    candidate = current[cut_position:] + remaining + current[:cut_position]
                    if candidate > max_string:
                        max_string = candidate

        return max_string