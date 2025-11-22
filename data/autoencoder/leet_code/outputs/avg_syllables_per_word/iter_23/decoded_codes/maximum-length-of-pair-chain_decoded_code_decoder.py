from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        current_end = float('-inf')
        chain_length = 0
        for pair in pairs:
            start, end = pair
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length