class Solution:
    def uniqueLetterString(self, s: str) -> int:
        MODULO_VALUE = 10**9 + 7
        string_length = len(s)

        list_last_positions = [-1] * 26
        list_second_last_positions = [-1] * 26

        total_result = 0

        for i, char in enumerate(s):
            index_position = ord(char) - ord('A')

            total_result += (i - list_last_positions[index_position]) * (list_last_positions[index_position] - list_second_last_positions[index_position])
            total_result %= MODULO_VALUE

            list_second_last_positions[index_position] = list_last_positions[index_position]
            list_last_positions[index_position] = i

        for i in range(26):
            total_result += (string_length - list_last_positions[i]) * (list_last_positions[i] - list_second_last_positions[i])
            total_result %= MODULO_VALUE

        return total_result