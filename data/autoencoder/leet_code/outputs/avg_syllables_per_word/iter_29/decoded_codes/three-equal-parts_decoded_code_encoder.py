from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = sum(arr)

        if total_ones == 0:
            return [0, 2]

        if total_ones % 3 != 0:
            return [-1, -1]

        part_ones = total_ones // 3

        first_part_index = 0
        count_ones = 0
        for i, val in enumerate(arr):
            if val == 1:
                count_ones += 1
                if count_ones == 1:
                    first_part_index = i
                if count_ones == part_ones:
                    break

        second_part_index = 0
        count_ones = 0
        for i, val in enumerate(arr):
            if val == 1:
                count_ones += 1
                if count_ones == part_ones + 1:
                    second_part_index = i
                    break

        third_part_index = 0
        count_ones = 0
        for i, val in enumerate(arr):
            if val == 1:
                count_ones += 1
                if count_ones == 2 * part_ones + 1:
                    third_part_index = i
                    break

        n = len(arr) - third_part_index

        if (first_part_index + n <= len(arr) and
            second_part_index + n <= len(arr) and
            arr[first_part_index:first_part_index + n] == arr[second_part_index:second_part_index + n] ==
            arr[third_part_index:]):
            return [first_part_index + n - 1, second_part_index + n]

        return [-1, -1]