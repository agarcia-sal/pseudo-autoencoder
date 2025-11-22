class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = []
        for num in range(1, n - k):
            result.append(num)
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