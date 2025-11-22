from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda element: element[1])
        current_end = float('-inf')
        chain_length = 0
        for element in pairs:
            start = element[0]
            end = element[1]
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length