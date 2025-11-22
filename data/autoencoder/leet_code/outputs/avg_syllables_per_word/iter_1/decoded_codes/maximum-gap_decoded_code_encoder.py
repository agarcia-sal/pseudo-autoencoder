def maxGap(nums):
    if len(nums) < 2:
        return 0

    def countingSort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for x in arr:
            count[(x // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in reversed(range(n)):
            idx = (arr[i] // exp) % 10
            output[count[idx] - 1] = arr[i]
            count[idx] -= 1

        for i in range(n):
            arr[i] = output[i]

    def radixSort(arr):
        maxV = max(arr)
        exp = 1
        while maxV // exp > 0:
            countingSort(arr, exp)
            exp *= 10

    radixSort(nums)
    maxDiff = 0
    for i in range(1, len(nums)):
        maxDiff = max(maxDiff, nums[i] - nums[i - 1])
    return maxDiff