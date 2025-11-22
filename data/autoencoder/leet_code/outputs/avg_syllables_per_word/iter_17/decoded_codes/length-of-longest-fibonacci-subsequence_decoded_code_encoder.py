from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        mapping_index = self.buildIndexMapping(arr)
        dictionary_dp = self.initializeDictionary()
        maximum_length = 0

        for k in range(len(arr)):
            for j in range(k):
                index_i = mapping_index.get(arr[k] - arr[j], -1)
                if 0 <= index_i < j:
                    dictionary_dp[j, k] = dictionary_dp.get((index_i, j), 2) + 1
                    maximum_length = max(maximum_length, dictionary_dp[j, k])

        return maximum_length if maximum_length >= 3 else 0

    def buildIndexMapping(self, arr: list[int]) -> dict[int, int]:
        # Create mapping from element to its index
        return {value: i for i, value in enumerate(arr)}

    def initializeDictionary(self) -> dict[tuple[int, int], int]:
        # Initialize empty dictionary to hold lengths of Fibonacci-like subsequences
        return {}