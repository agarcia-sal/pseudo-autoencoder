def find_peak_index(arr):
    L, R = 0, len(arr) - 1
    while L < R:
        M = (L + R) // 2
        if arr[M] < arr[M + 1]:
            L = M + 1
        else:
            R = M
    return L