from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = sum(arr)

        if total_ones == 0:
            return [0, 2]

        if total_ones % 3 != 0:
            return [-1, -1]

        part_ones = total_ones // 3

        n = len(arr)

        # Find the starting index of the first part
        first_part_index = 0
        count_ones = 0
        for i in range(n):
            if arr[i] == 1:
                count_ones += 1
                if count_ones == 1:
                    first_part_index = i
                if count_ones == part_ones:
                    break

        # Find the starting index of the second part
        second_part_index = 0
        count_ones = 0
        for i in range(n):
            if arr[i] == 1:
                count_ones += 1
                if count_ones == part_ones + 1:
                    second_part_index = i
                    break

        # Find the starting index of the third part
        third_part_index = 0
        count_ones = 0
        for i in range(n):
            if arr[i] == 1:
                count_ones += 1
                if count_ones == 2 * part_ones + 1:
                    third_part_index = i
                    break

        length = n - third_part_index

        if (first_part_index + length <= n and
            second_part_index + length <= n and
            arr[first_part_index:first_part_index+length] == arr[second_part_index:second_part_index+length] and
            arr[first_part_index:first_part_index+length] == arr[third_part_index:]):
            return [first_part_index + length - 1, second_part_index + length]

        return [-1, -1]