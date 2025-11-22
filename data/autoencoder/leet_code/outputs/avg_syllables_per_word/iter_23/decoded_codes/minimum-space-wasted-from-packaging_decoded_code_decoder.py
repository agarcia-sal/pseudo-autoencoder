from typing import List

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
                index = last_index
                while index < n and packages[index] <= box_size:
                    index += 1

                if index > last_index:
                    total_wasted += (index - last_index) * box_size - (prefix_sum[index] - prefix_sum[last_index])
                    last_index = index

                if last_index == n:
                    break

            if last_index == n:
                min_wasted_space = min(min_wasted_space, total_wasted)

        if min_wasted_space != float('inf'):
            return min_wasted_space % MOD
        else:
            return -1