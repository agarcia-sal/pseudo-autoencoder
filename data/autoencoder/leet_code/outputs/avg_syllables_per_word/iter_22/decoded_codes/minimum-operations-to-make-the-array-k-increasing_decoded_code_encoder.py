from bisect import bisect_right
from typing import List

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def longest_increasing_subsequence(subarr: List[int]) -> int:
            lis = []
            for num in subarr:
                # If lis is empty or num >= last element, append num
                if not lis or num >= lis[-1]:
                    lis.append(num)
                else:
                    # Find rightmost position to insert num to maintain sorted order
                    pos = bisect_right(lis, num)
                    lis[pos] = num
            return len(lis)

        total_operations = 0
        n = len(arr)

        for start in range(k):
            subarr = []
            for i in range(start, n, k):
                subarr.append(arr[i])
            lis_length = longest_increasing_subsequence(subarr)
            total_operations += len(subarr) - lis_length

        return total_operations