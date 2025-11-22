def max_chunks_to_sorted(arr):
    max_so_far = 0
    chunks = 0
    for i in range(len(arr)):
        max_so_far = max(max_so_far, arr[i])
        if max_so_far == i:
            chunks += 1
    return chunks