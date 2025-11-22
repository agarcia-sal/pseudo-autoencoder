class Solution:
    def constructArray(self, n, k):
        result = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            if left == right:
                result.append(left)
            else:
                result.extend([left, right])
            left += 1
            right -= 1
        return result