def apply_updates(length, updates):
    diff = [0] * (length + 1)
    for start, end, inc in updates:
        diff[start] += inc
        if end + 1 < length:
            diff[end + 1] -= inc
    arr = [0] * length
    arr[0] = diff[0]
    for i in range(1, length):
        arr[i] = arr[i-1] + diff[i]
    return arr