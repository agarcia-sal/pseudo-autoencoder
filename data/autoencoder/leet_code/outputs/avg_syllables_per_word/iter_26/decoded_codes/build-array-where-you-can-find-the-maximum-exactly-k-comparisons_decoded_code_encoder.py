class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MODULO = 10**9 + 7

        # dp[length][max_element][cost] = number of arrays of 'length'
        # with 'max_element' as the max and 'cost' search cost
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Base case: arrays of length 1 have cost 1 and max_element equal to the element itself
        for max_element in range(1, m + 1):
            dp[1][max_element][1] = 1

        for length in range(2, n + 1):
            for max_element in range(1, m + 1):
                for cost in range(1, k + 1):
                    # Append an element smaller than max_element -> cost increases by 1
                    # Summing over smaller_max < max_element contributing from dp[length-1][smaller_max][cost-1]
                    acc = 0
                    for smaller_max in range(1, max_element):
                        acc += dp[length - 1][smaller_max][cost - 1]
                    dp[length][max_element][cost] = (dp[length][max_element][cost] + acc) % MODULO
                    # Append the max_element again -> cost stays the same
                    dp[length][max_element][cost] = (dp[length][max_element][cost] + dp[length - 1][max_element][cost] * max_element) % MODULO

        total_result = 0
        for max_element in range(1, m + 1):
            total_result = (total_result + dp[n][max_element][k]) % MODULO

        return total_result