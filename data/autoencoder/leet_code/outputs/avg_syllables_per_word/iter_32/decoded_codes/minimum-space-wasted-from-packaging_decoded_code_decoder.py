from typing import List
import bisect

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10**9 + 7
        packages.sort()
        n = len(packages)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]

        min_wasted_space = float('inf')

        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue

            total_wasted = 0
            last_index = 0

            for box_size in box:
                # use bisect_right to find the first index in packages
                # that is greater than box_size
                index = bisect.bisect_right(packages, box_size, last_index, n)

                if index > last_index:
                    # waste = number of packages * box_size - sum of package sizes
                    total_wasted += (index - last_index) * box_size - (prefix_sum[index] - prefix_sum[last_index])
                    last_index = index

                if last_index == n:
                    # all packages covered, no need to continue scanning smaller boxes
                    break

            if last_index == n and total_wasted < min_wasted_space:
                min_wasted_space = total_wasted

        return -1 if min_wasted_space == float('inf') else min_wasted_space % MOD