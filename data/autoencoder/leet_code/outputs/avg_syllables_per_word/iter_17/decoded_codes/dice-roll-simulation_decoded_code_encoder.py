class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7

        # Initialize dp array with dimensions (n+1) x 6 x (max rollMax + 1)
        dp = initialize_dp(n, rollMax)

        # Base case: for each face, one way to roll it once
        for face_index in range(6):
            dp[1][face_index][1] = 1

        for roll_count in range(2, n + 1):
            for face_index in range(6):
                max_consec = rollMax[face_index]
                for consecutive_count in range(1, max_consec + 1):
                    if consecutive_count > 1:
                        # Continue same face sequence by incrementing consecutive_count
                        dp[roll_count][face_index][consecutive_count] = dp[roll_count - 1][face_index][consecutive_count - 1] % MOD
                    else:
                        # Start a new face sequence after different face
                        temp_sum = 0
                        for previous_face in range(6):
                            if previous_face != face_index:
                                prev_max_consec = rollMax[previous_face]
                                for prev_consec_count in range(1, prev_max_consec + 1):
                                    temp_sum += dp[roll_count - 1][previous_face][prev_consec_count]
                        dp[roll_count][face_index][consecutive_count] = temp_sum % MOD

        total_ways = 0
        for face_index in range(6):
            for consecutive_count in range(1, rollMax[face_index] + 1):
                total_ways += dp[n][face_index][consecutive_count]
        return total_ways % MOD

def initialize_dp(n: int, rollMax: list[int]) -> list[list[list[int]]]:
    # Create a 3D list: (n+1) x 6 x (max rollMax +1) zero-initialized
    max_roll = max(rollMax)
    return [[[0]*(max_roll+1) for _ in range(6)] for _ in range(n+1)]