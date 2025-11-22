class Solution:
    def findLongestChain(self, pairs):
        self.sort_pairs_by_second_element(pairs)
        current_end = float('-inf')
        chain_length = 0
        for start, end in pairs:
            if start > current_end:
                current_end = end
                chain_length += 1
        return chain_length

    def sort_pairs_by_second_element(self, pairs):
        pairs.sort(key=lambda x: x[1])