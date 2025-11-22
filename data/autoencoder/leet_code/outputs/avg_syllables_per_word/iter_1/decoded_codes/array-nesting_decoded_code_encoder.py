def array_nesting(nums):
    n = len(nums)
    visited = [False] * n
    max_len = 0
    for i in range(n):
        if not visited[i]:
            length = 0
            k = i
            while not visited[k]:
                visited[k] = True
                k = nums[k]
                length += 1
            max_len = max(max_len, length)
    return max_len