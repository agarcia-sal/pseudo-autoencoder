import heapq

def smallest_range(nums):
    min_heap = []
    max_val = float('-inf')

    for i in range(len(nums)):
        heapq.heappush(min_heap, (nums[i][0], i, 0))
        max_val = max(max_val, nums[i][0])

    smallest_range = float('inf')
    result = [-100000, 100000]

    while min_heap:
        min_val, i, j = heapq.heappop(min_heap)
        if max_val - min_val < smallest_range:
            smallest_range = max_val - min_val
            result = [min_val, max_val]
        if j + 1 < len(nums[i]):
            next_val = nums[i][j+1]
            heapq.heappush(min_heap, (next_val, i, j+1))
            max_val = max(max_val, next_val)
        else:
            break

    return result