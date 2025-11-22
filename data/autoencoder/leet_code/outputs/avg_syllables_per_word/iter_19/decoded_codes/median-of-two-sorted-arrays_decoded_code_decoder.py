from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = -inf if partitionX == 0 else nums1[partitionX - 1]
            minRightX = inf if partitionX == x else nums1[partitionX]

            maxLeftY = -inf if partitionY == 0 else nums2[partitionY - 1]
            minRightY = inf if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    maximum_of_left = max(maxLeftX, maxLeftY)
                    minimum_of_right = min(minRightX, minRightY)
                    median_value = (maximum_of_left + minimum_of_right) / 2
                    return median_value
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1