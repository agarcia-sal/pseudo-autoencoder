class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        sum_steps = 0
        # Increment steps until sum_steps >= target
        while sum_steps < target:
            k += 1
            sum_steps += k
        # Check if difference is even
        if (sum_steps - target) % 2 == 0:
            return k
        else:
            # Adjust k according to parity
            if k % 2 == 0:
                return k + 1
            else:
                return k + 2