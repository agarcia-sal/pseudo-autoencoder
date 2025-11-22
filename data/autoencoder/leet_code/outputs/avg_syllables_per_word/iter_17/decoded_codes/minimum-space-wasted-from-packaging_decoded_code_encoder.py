from typing import List
import math
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)

        prefix_sum = self.initializePrefixSum(n)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]

        min_wasted_space = math.inf

        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue

            total_wasted = 0
            last_index = 0

            for box_size in box:
                # Find the index of the first package that cannot fit into box_size
                index = bisect.bisect_right(packages, box_size, last_index, n)

                if index > last_index:
                    total_wasted += (index - last_index) * box_size - (prefix_sum[index] - prefix_sum[last_index])
                    last_index = index

                if last_index == n:
                    break

            if last_index == n:
                min_wasted_space = min(min_wasted_space, total_wasted)

        return min_wasted_space % MOD if min_wasted_space != math.inf else -1

    def initializePrefixSum(self, length: int) -> List[int]:
        return [0] * (length + 1)