class Solution:
    def minimumBoxes(self, n: int) -> int:
        def triangular_pyramid(k: int) -> int:
            # Returns the total number of boxes in a triangular pyramid with k layers
            return (k * (k + 1) * (k + 2)) // 6

        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if triangular_pyramid(mid) <= n:
                left = mid
            else:
                right = mid - 1

        boxes_used = triangular_pyramid(left)
        remaining = n - boxes_used
        floor_boxes = (left * (left + 1)) // 2

        additional_boxes = 0
        while remaining > 0:
            additional_boxes += 1
            remaining -= additional_boxes

        return floor_boxes + additional_boxes