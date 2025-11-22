class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        def countingSort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                digit_index = (arr[i] // exp) % 10
                count[digit_index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                digit_index = (arr[i] // exp) % 10
                output[count[digit_index] - 1] = arr[i]
                count[digit_index] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        def radixSort(arr):
            max_value = max(arr)
            exp = 1
            while max_value // exp > 0:
                countingSort(arr, exp)
                exp *= 10

        radixSort(nums)

        max_diff = 0
        for i in range(1, len(nums)):
            current_diff = nums[i] - nums[i - 1]
            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff