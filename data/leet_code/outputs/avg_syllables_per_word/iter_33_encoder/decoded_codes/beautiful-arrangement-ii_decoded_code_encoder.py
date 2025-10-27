class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = []
        for number in range(1, n - k):
            result.append(number)
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