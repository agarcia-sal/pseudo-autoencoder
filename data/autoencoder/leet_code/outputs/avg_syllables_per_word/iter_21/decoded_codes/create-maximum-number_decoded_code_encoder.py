class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxSingleArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1, arr2):
            result = []
            arr1, arr2 = arr1[:], arr2[:]  # copy to avoid modifying inputs
            while arr1 or arr2:
                # Compare lex order of remaining arr1 and arr2
                if arr1 > arr2:
                    result.append(arr1.pop(0))
                else:
                    result.append(arr2.pop(0))
            return result

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and k - i <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number