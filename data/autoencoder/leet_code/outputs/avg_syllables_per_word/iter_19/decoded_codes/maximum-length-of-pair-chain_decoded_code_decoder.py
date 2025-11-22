from math import inf

class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        current_end = -inf
        chain_length = 0
        for start, end in pairs:
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length