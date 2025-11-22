from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    left_max = max(maxLeftX, maxLeftY)
                    right_min = min(minRightX, minRightY)
                    return (left_max + right_min) / 2.0
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        # If input arrays are not sorted or input is invalid, raise an error
        raise ValueError("Input arrays are not sorted or invalid input.")