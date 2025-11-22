class Solution:
    def numDecodings(self, string_input: str) -> int:
        if not string_input or string_input[0] == '0':
            return 0
        n = len(string_input)
        decoding_ways_list = [0] * (n + 1)
        decoding_ways_list[0] = 1
        decoding_ways_list[1] = 1
        for index in range(2, n + 1):
            if string_input[index - 1] != '0':
                decoding_ways_list[index] += decoding_ways_list[index - 1]
            two_digit_number = int(string_input[index - 2:index])
            if 10 <= two_digit_number <= 26:
                decoding_ways_list[index] += decoding_ways_list[index - 2]
        return decoding_ways_list[-1]