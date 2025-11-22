from math import inf

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)
        low = 0
        high = x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = -inf if partitionX == 0 else nums1[partitionX - 1]
            minRightX = inf if partitionX == x else nums1[partitionX]

            maxLeftY = -inf if partitionY == 0 else nums2[partitionY - 1]
            minRightY = inf if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    maximum_of_lefts = maxLeftX if maxLeftX > maxLeftY else maxLeftY
                    minimum_of_rights = minRightX if minRightX < minRightY else minRightY
                    return (maximum_of_lefts + minimum_of_rights) / 2
                else:
                    return maxLeftX if maxLeftX > maxLeftY else maxLeftY
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1