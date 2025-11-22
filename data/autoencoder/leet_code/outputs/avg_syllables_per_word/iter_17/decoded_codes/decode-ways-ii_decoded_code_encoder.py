class Solution:
    def numDecodings(self, string_s: str) -> int:
        MODULO = 10**9 + 7
        n = len(string_s)
        dp_list = [0] * (n + 1)
        dp_list[0] = 1

        def ways_to_decode_single(character_char: str) -> int:
            if character_char == '*':
                return 9
            elif character_char == '0':
                return 0
            else:
                return 1

        def ways_to_decode_pair(character_char1: str, character_char2: str) -> int:
            if character_char1 == '*' and character_char2 == '*':
                # '**' can represent 11-19 and 21-26: total 15 possibilities
                return 15
            elif character_char1 == '*':
                # First char '*', second is digit
                if '0' <= character_char2 <= '6':
                    return 2  # '*0'-'*6' can be either '1x' or '2x'
                else:
                    return 1  # '*7'-'*9' can only be '1x'
            elif character_char2 == '*':
                # First char digit, second is '*'
                if character_char1 == '1':
                    return 9  # '1*' can be 11-19
                elif character_char1 == '2':
                    return 6  # '2*' can be 21-26
                else:
                    return 0
            else:
                number_value = self.ConvertCharsToInt(character_char1, character_char2)
                if 10 <= number_value <= 26:
                    return 1
                else:
                    return 0

        for index_i in range(1, n + 1):
            single_char = string_s[index_i - 1]
            dp_list[index_i] += dp_list[index_i - 1] * ways_to_decode_single(single_char)
            dp_list[index_i] %= MODULO

            if index_i > 1:
                char1 = string_s[index_i - 2]
                char2 = string_s[index_i - 1]
                dp_list[index_i] += dp_list[index_i - 2] * ways_to_decode_pair(char1, char2)
                dp_list[index_i] %= MODULO

        return dp_list[-1]

    def ConvertCharsToInt(self, character_char1: str, character_char2: str) -> int:
        # Converts two digit characters into an integer
        return int(character_char1) * 10 + int(character_char2)