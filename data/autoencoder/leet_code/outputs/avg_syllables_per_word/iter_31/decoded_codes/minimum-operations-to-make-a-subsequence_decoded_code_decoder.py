from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Map each value in target to its index
        mapping = {value: idx for idx, value in enumerate(target)}

        # Transform arr elements to their indices in target if present
        transformed_arr = [mapping[val] for val in arr if val in mapping]

        # Compute length of LIS on transformed_arr
        lis = []
        for num in transformed_arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        lcs_length = len(lis)
        return len(target) - lcs_length