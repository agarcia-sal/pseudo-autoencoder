class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MODULO_VALUE = 10**9 + 7

        # dp[roll_index][face_index][consecutive_count]
        # roll_index : 1 to n (inclusive)
        # face_index : 0 to 5 (six faces)
        # consecutive_count : 1 to rollMax[face_index]
        dp = [[[0] * (rollMax[face] + 1) for face in range(6)] for _ in range(n + 1)]

        # Initialize for the first roll: one way to have each face with consecutive_count = 1
        for face in range(6):
            dp[1][face][1] = 1

        for roll_index in range(2, n + 1):
            for face_index in range(6):
                max_consec = rollMax[face_index]
                for consec_count in range(1, max_consec + 1):
                    if consec_count > 1:
                        # Continue rolling the same face consecutively
                        dp[roll_index][face_index][consec_count] = dp[roll_index - 1][face_index][consec_count - 1] % MODULO_VALUE
                    else:
                        # Start a new sequence for this face
                        total_ways = 0
                        for other_face in range(6):
                            if other_face != face_index:
                                max_other = rollMax[other_face]
                                for other_consec in range(1, max_other + 1):
                                    total_ways = (total_ways + dp[roll_index - 1][other_face][other_consec]) % MODULO_VALUE
                        dp[roll_index][face_index][1] = total_ways

        total_ways = 0
        for face_index in range(6):
            max_consec = rollMax[face_index]
            for consec_count in range(1, max_consec + 1):
                total_ways = (total_ways + dp[n][face_index][consec_count]) % MODULO_VALUE

        return total_ways