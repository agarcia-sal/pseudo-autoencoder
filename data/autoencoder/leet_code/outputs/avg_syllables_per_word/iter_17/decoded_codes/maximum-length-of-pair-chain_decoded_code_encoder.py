class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])
        current_end = float('-inf')
        chain_length = 0
        for start, end in pairs:
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length