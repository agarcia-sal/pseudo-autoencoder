class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        sum_steps = 0

        while sum_steps < target:
            k += 1
            sum_steps += k

        if (sum_steps - target) % 2 == 0:
            return k
        else:
            if k % 2 == 0:
                return k + 1
            else:
                return k + 2