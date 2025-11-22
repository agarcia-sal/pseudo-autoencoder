from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    maximum_value = max(maxLeftX, maxLeftY)
                    minimum_value = min(minRightX, minRightY)
                    median_value = (maximum_value + minimum_value) / 2
                    return median_value
                else:
                    maximum_value = max(maxLeftX, maxLeftY)
                    return maximum_value
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1