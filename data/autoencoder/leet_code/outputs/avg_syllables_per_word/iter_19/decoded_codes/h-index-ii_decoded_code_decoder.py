class Solution:
    def hIndex(self, citations):
        n = len(citations)
        left = 0
        right = n - 1
        h_index = 0

        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                h_index = n - mid
                right = mid - 1
            else:
                left = mid + 1

        return h_index