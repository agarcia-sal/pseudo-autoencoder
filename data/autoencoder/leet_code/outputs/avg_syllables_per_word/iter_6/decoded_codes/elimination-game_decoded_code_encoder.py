class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining, step, head = n, 1, 1
        left_to_right = True

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left_to_right = not left_to_right

        return head