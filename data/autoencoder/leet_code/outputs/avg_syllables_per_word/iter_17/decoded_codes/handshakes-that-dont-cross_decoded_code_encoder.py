class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MODULO = 10**9 + 7
        dp_list = [0] * (numPeople + 1)
        dp_list[0] = 1
        dp_list[2] = 1

        for i in range(4, numPeople + 1, 2):
            for j in range(0, i, 2):
                dp_list[i] = (dp_list[i] + dp_list[j] * dp_list[i - 2 - j]) % MODULO

        return dp_list[numPeople]