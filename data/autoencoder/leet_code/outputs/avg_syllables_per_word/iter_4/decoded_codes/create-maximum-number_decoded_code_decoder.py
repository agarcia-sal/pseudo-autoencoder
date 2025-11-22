class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxSingleArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1, arr2):
            merged = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                # Compare the remaining slices lex order
                if arr1[i:] > arr2[j:]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            return merged

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k+1):
            if i <= len1 and k - i <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number