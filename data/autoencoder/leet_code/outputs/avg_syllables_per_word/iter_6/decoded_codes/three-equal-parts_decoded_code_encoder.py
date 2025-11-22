class Solution:
    def threeEqualParts(self, arr):
        total_ones = sum(arr)
        if total_ones == 0:
            return [0, 2]
        if total_ones % 3 != 0:
            return [-1, -1]

        part_ones = total_ones // 3
        n = len(arr)

        def find_index(target):
            count = 0
            for i, val in enumerate(arr):
                if val == 1:
                    count += 1
                    if count == target:
                        return i
            return -1

        first_part_index = find_index(1)
        second_part_index = find_index(part_ones + 1)
        third_part_index = find_index(2 * part_ones + 1)

        length = n - third_part_index
        if (first_part_index + length <= n and
            second_part_index + length <= n and
            arr[first_part_index:first_part_index + length] == arr[second_part_index:second_part_index + length] == arr[third_part_index:]):
            return [first_part_index + length - 1, second_part_index + length]
        else:
            return [-1, -1]