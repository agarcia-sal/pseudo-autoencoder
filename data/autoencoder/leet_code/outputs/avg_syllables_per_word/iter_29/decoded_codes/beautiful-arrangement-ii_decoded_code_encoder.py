class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result = []
        for current_number in range(1, n - k):
            result.append(current_number)
        left_pointer = n - k
        right_pointer = n
        while left_pointer <= right_pointer:
            if left_pointer == right_pointer:
                result.append(left_pointer)
            else:
                result.append(left_pointer)
                result.append(right_pointer)
            left_pointer += 1
            right_pointer -= 1
        return result