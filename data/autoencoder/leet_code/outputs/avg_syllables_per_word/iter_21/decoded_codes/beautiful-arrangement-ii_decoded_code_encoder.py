class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            if left == right:
                result.append(left)
            else:
                result.append(left)
                result.append(right)
            left += 1
            right -= 1
        return result