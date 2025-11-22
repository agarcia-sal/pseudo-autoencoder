class Solution:
    def distinctSubseqII(self, string_s: str) -> int:
        MODULO_VALUE = 10**9 + 7
        length_n = len(string_s)
        dynamic_programming_list = [0] * (length_n + 1)
        dynamic_programming_list[0] = 1
        last_occurrence_map = {}

        for index_i in range(1, length_n + 1):
            current_character = string_s[index_i - 1]
            dynamic_programming_list[index_i] = (2 * dynamic_programming_list[index_i - 1]) % MODULO_VALUE
            if current_character in last_occurrence_map:
                previous_index = last_occurrence_map[current_character]
                dynamic_programming_list[index_i] = (dynamic_programming_list[index_i] - dynamic_programming_list[previous_index - 1] + MODULO_VALUE) % MODULO_VALUE
            last_occurrence_map[current_character] = index_i

        result = (dynamic_programming_list[length_n] - 1) % MODULO_VALUE
        return result