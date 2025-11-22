class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_index = min(steps // 2, arrLen - 1)
        dp = self.initialize_dp_list(max_index)
        self.set_initial_dp_state(dp)
        for _ in range(1, steps + 1):
            prev_dp = self.create_copy_of_dp(dp)
            for i in range(max_index + 1):
                self.set_dp_same_position(dp, prev_dp, i)
                if i > 0:
                    self.add_left_position_ways(dp, prev_dp, i, MOD)
                if i < max_index:
                    self.add_right_position_ways(dp, prev_dp, i, MOD)
        return dp[0]

    def initialize_dp_list(self, max_index: int) -> list[int]:
        return [0] * (max_index + 1)

    def set_initial_dp_state(self, dp: list[int]) -> None:
        dp[0] = 1

    def create_copy_of_dp(self, dp: list[int]) -> list[int]:
        return dp.copy()

    def set_dp_same_position(self, dp: list[int], prev_dp: list[int], i: int) -> None:
        dp[i] = prev_dp[i]

    def add_left_position_ways(self, dp: list[int], prev_dp: list[int], i: int, MOD: int) -> None:
        dp[i] = (dp[i] + prev_dp[i - 1]) % MOD

    def add_right_position_ways(self, dp: list[int], prev_dp: list[int], i: int, MOD: int) -> None:
        dp[i] = (dp[i] + prev_dp[i + 1]) % MOD