from bisect import bisect_right
from math import inf

class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        MODULO = 10**9 + 7

        packages.sort()
        total_packages = len(packages)

        prefix_sum = [0] * (total_packages + 1)
        for i in range(total_packages):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]

        minimum_wasted_space = inf

        for box_list in boxes:
            box_list.sort()

            if box_list[-1] < packages[-1]:
                continue

            total_wasted_space = 0
            last_package_index = 0

            for box_size in box_list:
                current_index = bisect_right(packages, box_size, last_package_index, total_packages)

                if current_index > last_package_index:
                    total_wasted_space += box_size * (current_index - last_package_index) - (prefix_sum[current_index] - prefix_sum[last_package_index])
                    last_package_index = current_index

                if last_package_index == total_packages:
                    break

            if last_package_index == total_packages:
                minimum_wasted_space = min(minimum_wasted_space, total_wasted_space)

        return minimum_wasted_space % MODULO if minimum_wasted_space != inf else -1