class Solution:
    def findClosestElements(self, arr, k, x):
        import bisect
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1

        while right - left - 1 < k:
            if left == -1 or (right < len(arr) and abs(arr[right] - x) < abs(arr[left] - x)):
                right += 1
            else:
                left -= 1
        return arr[left + 1:right]