def max_distance(arrays):
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_distance = 0

    for array in arrays[1:]:
        current_min = array[0]
        current_max = array[-1]
        max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))
        min_val = min(min_val, current_min)
        max_val = max(max_val, current_max)

    return max_distance