class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) == 0:
            return 0

        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            char = chars[read_index]
            count = 0

            while read_index < n and chars[read_index] == char:
                read_index += 1
                count += 1

            chars[write_index] = char
            write_index += 1

            if count > 1:
                for digit_char in str(count):
                    chars[write_index] = digit_char
                    write_index += 1

        return write_index