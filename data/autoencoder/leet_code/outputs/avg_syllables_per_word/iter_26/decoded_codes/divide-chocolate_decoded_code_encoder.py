class Solution:
    def maximizeSweetness(self, sweetness, k):
        def canDivide(min_sweet):
            pieces = 0
            current_sweet = 0
            for sweet in sweetness:
                current_sweet += sweet
                if current_sweet >= min_sweet:
                    pieces += 1
                    current_sweet = 0
                    if pieces > k:
                        return True
            return pieces > k

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result