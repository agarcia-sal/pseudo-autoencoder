from bisect import bisect_right
from typing import List

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:

        def longest_increasing_subsequence(subarr: List[int]) -> int:
            lis = []
            for number in subarr:
                if not lis or number >= lis[-1]:
                    lis.append(number)
                else:
                    pos = bisect_right(lis, number)
                    lis[pos] = number
            return len(lis)

        total_operations = 0
        n = len(arr)

        for start in range(k):
            subarr = [arr[i] for i in range(start, n, k)]
            lis_length = longest_increasing_subsequence(subarr)
            total_operations += len(subarr) - lis_length

        return total_operations