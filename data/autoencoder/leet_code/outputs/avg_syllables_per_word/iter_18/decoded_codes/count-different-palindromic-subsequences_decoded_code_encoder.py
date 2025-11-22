class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MODULO_DIVISOR = 10**9 + 7
        length_of_s = len(s)

        next_occurrence = [[-1] * length_of_s for _ in range(4)]
        prev_occurrence = [[-1] * length_of_s for _ in range(4)]

        for numeric_character_index in range(4):
            character_to_check = chr(ord('a') + numeric_character_index)
            last_recorded_position = -1
            for index_in_s in range(length_of_s):
                if s[index_in_s] == character_to_check:
                    last_recorded_position = index_in_s
                prev_occurrence[numeric_character_index][index_in_s] = last_recorded_position

            last_recorded_position = -1
            for index_in_s_reversed in range(length_of_s - 1, -1, -1):
                if s[index_in_s_reversed] == character_to_check:
                    last_recorded_position = index_in_s_reversed
                next_occurrence[numeric_character_index][index_in_s_reversed] = last_recorded_position

        dp = [[0] * length_of_s for _ in range(length_of_s)]

        for single_index in range(length_of_s):
            dp[single_index][single_index] = 1

        for subsequence_length in range(2, length_of_s + 1):
            for start_index in range(length_of_s - subsequence_length + 1):
                end_index = start_index + subsequence_length - 1
                for numeric_character_index in range(4):
                    character_to_check = chr(ord('a') + numeric_character_index)
                    left_position = next_occurrence[numeric_character_index][start_index]
                    right_position = prev_occurrence[numeric_character_index][end_index]

                    if left_position > end_index or right_position < start_index or left_position == -1 or right_position == -1:
                        continue
                    elif left_position == right_position:
                        dp[start_index][end_index] = (dp[start_index][end_index] + 1) % MODULO_DIVISOR
                    else:
                        dp[start_index][end_index] = (dp[start_index][end_index] + dp[left_position + 1][right_position - 1] + 2) % MODULO_DIVISOR

        return dp[0][length_of_s - 1] if length_of_s > 0 else 0