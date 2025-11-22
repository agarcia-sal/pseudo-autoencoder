from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = self.sort_the_pairs_by_second_element(pairs)
        current_end = float('-inf')
        chain_length = 0
        for pair in pairs:
            start, end = pair
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length

    def sort_the_pairs_by_second_element(self, input_pairs: List[List[int]]) -> List[List[int]]:
        return sorted(input_pairs, key=lambda x: x[1])