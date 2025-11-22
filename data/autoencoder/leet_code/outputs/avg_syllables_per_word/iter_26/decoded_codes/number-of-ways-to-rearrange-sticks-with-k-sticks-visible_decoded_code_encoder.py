class Solution:
    def rearrangeSticks(self, number_of_sticks: int, number_of_visible_sticks: int) -> int:
        modulus_value = 10**9 + 1
        dp_table = [[0] * (number_of_visible_sticks + 1) for _ in range(number_of_sticks + 1)]
        dp_table[0][0] = 1

        for index_i in range(1, number_of_sticks + 1):
            for index_j in range(1, number_of_visible_sticks + 1):
                dp_table[index_i][index_j] = (
                    dp_table[index_i - 1][index_j - 1] +
                    (index_i - 1) * dp_table[index_i - 1][index_j]
                ) % modulus_value

        return dp_table[number_of_sticks][number_of_visible_sticks]