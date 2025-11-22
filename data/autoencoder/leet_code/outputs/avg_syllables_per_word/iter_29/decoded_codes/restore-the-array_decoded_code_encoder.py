class Solution:
    def numberOfArrays(self, input_string: str, limit_k: int) -> int:
        MOD = 10**9 + 7
        length_n = len(input_string)
        dp_list = [0] * (length_n + 1)
        dp_list[0] = 1
        for position_i in range(1, length_n + 1):
            for position_j in range(position_i):
                if input_string[position_j] == '0':
                    continue
                substring = input_string[position_j:position_i]
                num = int(substring)
                if 1 <= num <= limit_k:
                    dp_list[position_i] = (dp_list[position_i] + dp_list[position_j]) % MOD
        return dp_list[length_n]