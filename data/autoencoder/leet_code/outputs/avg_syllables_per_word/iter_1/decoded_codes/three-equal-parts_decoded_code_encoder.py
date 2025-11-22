def three_equal_parts(arr):
    total_ones = sum(arr)
    if total_ones == 0:
        return [0, 2]
    if total_ones % 3 != 0:
        return [-1, -1]

    part_ones = total_ones // 3

    ones_indices = [i for i, bit in enumerate(arr) if bit == 1]
    first = ones_indices[0]
    second = ones_indices[part_ones]
    third = ones_indices[2 * part_ones]

    length = len(arr) - third
    if arr[first:first+length] == arr[second:second+length] == arr[third:]:
        return [first + length - 1, second + length]
    else:
        return [-1, -1]