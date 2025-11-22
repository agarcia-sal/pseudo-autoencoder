from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        def countingSort(arr: List[int], exp: int) -> None:
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                division_result = arr[i] // exp
                digit = division_result % 10
                count[digit] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                division_result = arr[i] // exp
                digit = division_result % 10
                output[count[digit] - 1] = arr[i]
                count[digit] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]

        def radixSort(arr: List[int]) -> None:
            max1 = max(arr)
            exp = 1
            while max1 // exp > 0:
                countingSort(arr, exp)
                exp *= 10

        radixSort(nums)

        max_diff = 0
        for i in range(1, len(nums)):
            current_gap = nums[i] - nums[i - 1]
            if current_gap > max_diff:
                max_diff = current_gap

        return max_diff