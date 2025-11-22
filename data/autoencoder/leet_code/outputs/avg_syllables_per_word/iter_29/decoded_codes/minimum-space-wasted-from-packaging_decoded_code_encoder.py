from bisect import bisect_right
from math import inf

class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        MOD = 10**9 + 1
        packages.sort()
        n = len(packages)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]

        min_wasted_space = inf

        for box_supplier in boxes:
            box_supplier.sort()
            if box_supplier[-1] < packages[-1]:
                continue

            total_wasted = 0
            last_index = 0

            for box_size in box_supplier:
                index = bisect_right(packages, box_size, last_index, n)
                if index > last_index:
                    wasted_for_current_box = (index - last_index) * box_size - (prefix_sum[index] - prefix_sum[last_index])
                    total_wasted += wasted_for_current_box
                    last_index = index

            if last_index == n:
                min_wasted_space = min(min_wasted_space, total_wasted)

        return min_wasted_space % MOD if min_wasted_space != inf else -1