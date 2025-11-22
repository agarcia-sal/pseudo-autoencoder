class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int, n: int) -> int:
            steps = 0
            next_prefix = prefix + 1
            while prefix <= n:
                steps += min(n - prefix + 1, next_prefix - prefix)
                prefix *= 10
                next_prefix *= 10
            return steps

        current = 1
        k -= 1

        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current