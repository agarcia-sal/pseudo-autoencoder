class Solution:
    def uniqueLetterString(self, s):
        MODULO = 10**9 + 7
        string_length = len(s)
        # last_positions and second_last_positions track the last two occurrences of each uppercase letter
        last_positions = [-1] * 26
        second_last_positions = [-1] * 26
        total_result = 0

        for index, character in enumerate(s):
            character_index = ord(character) - ord('A')
            contribution = (index - last_positions[character_index]) * (last_positions[character_index] - second_last_positions[character_index])
            total_result = (total_result + contribution) % MODULO
            second_last_positions[character_index] = last_positions[character_index]
            last_positions[character_index] = index

        for i in range(26):
            contribution = (string_length - last_positions[i]) * (last_positions[i] - second_last_positions[i])
            total_result = (total_result + contribution) % MODULO

        return total_result