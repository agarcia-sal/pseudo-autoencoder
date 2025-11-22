class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MODULO_CONSTANT = 10**9 + 7

        # Initialize a 3D list dp with dimensions (n+1) x (m+1) x (k+1) filled with zeros
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Base case: For arrays of length 1, each possible max element (1 to m) can form exactly one array
        for max_element in range(1, m + 1):
            dp[1][max_element][1] = 1

        for array_length in range(2, n + 1):
            for max_element in range(1, m + 1):
                for search_cost in range(1, k + 1):
                    # Add arrays where max element increases (smaller max elements with cost - 1)
                    for smaller_max_element in range(1, max_element):
                        dp[array_length][max_element][search_cost] += dp[array_length - 1][smaller_max_element][search_cost - 1]
                        dp[array_length][max_element][search_cost] %= MODULO_CONSTANT

                    # Add arrays where max element remains the same
                    dp[array_length][max_element][search_cost] += dp[array_length - 1][max_element][search_cost] * max_element
                    dp[array_length][max_element][search_cost] %= MODULO_CONSTANT

        total_result = 0
        for max_element_result in range(1, m + 1):
            total_result += dp[n][max_element_result][k]
            total_result %= MODULO_CONSTANT

        return total_result