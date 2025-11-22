class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MODULO_VALUE = 10**9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        for max_element_index in range(1, m + 1):
            dp[1][max_element_index][1] = 1

        for array_length in range(2, n + 1):
            for max_element_index in range(1, m + 1):
                for search_cost_value in range(1, k + 1):
                    cum_sum = 0
                    for smaller_max_element in range(1, max_element_index):
                        cum_sum += dp[array_length - 1][smaller_max_element][search_cost_value - 1]
                    cum_sum %= MODULO_VALUE
                    dp[array_length][max_element_index][search_cost_value] = cum_sum

                    dp[array_length][max_element_index][search_cost_value] += dp[array_length - 1][max_element_index][search_cost_value] * max_element_index
                    dp[array_length][max_element_index][search_cost_value] %= MODULO_VALUE

        total_result = 0
        for max_element_index in range(1, m + 1):
            total_result += dp[n][max_element_index][k]
        return total_result % MODULO_VALUE