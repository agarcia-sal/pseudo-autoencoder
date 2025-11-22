from bisect import bisect_right
from math import inf

class Solution:
    def minWastedSpace(self, packages, boxes):
        MODULO_VALUE = 10**9 + 1
        packages.sort()
        number_of_packages = len(packages)

        prefix_sum = [0] * (number_of_packages + 1)
        for i in range(number_of_packages):
            prefix_sum[i + 1] = prefix_sum[i] + packages[i]

        minimal_wasted_space = inf

        for box_supplier in boxes:
            box_supplier.sort()
            if box_supplier[-1] < packages[-1]:
                continue

            total_wasted_space = 0
            last_package_index = 0

            for box_size in box_supplier:
                # Find the rightmost index where box_size can fit the packages
                index = bisect_right(packages, box_size, lo=last_package_index)
                if index > last_package_index:
                    total_wasted_space += (index - last_package_index) * box_size - (prefix_sum[index] - prefix_sum[last_package_index])
                    last_package_index = index
                if last_package_index == number_of_packages:
                    break

            if last_package_index == number_of_packages:
                minimal_wasted_space = min(minimal_wasted_space, total_wasted_space)

        if minimal_wasted_space == inf:
            return -1
        else:
            return minimal_wasted_space % MODULO_VALUE