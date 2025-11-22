class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int, n: int) -> int:
            next_prefix = prefix + 1
            steps = 0
            while prefix <= n:
                temp_difference = n - prefix + 1
                interval_width = next_prefix - prefix
                steps += temp_difference if temp_difference < interval_width else interval_width
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