def max_chunks_to_sorted(arr):
    max_so_far = []
    cur_max = arr[0]
    for num in arr:
        cur_max = max(cur_max, num)
        max_so_far.append(cur_max)

    sorted_arr = sorted(arr)
    chunks = 0
    max_chunk = float('-inf')
    for i in range(len(arr)):
        max_chunk = max(max_chunk, arr[i])
        if max_chunk == sorted_arr[i]:
            chunks += 1
    return chunks