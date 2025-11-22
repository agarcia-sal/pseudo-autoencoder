class Solution:
    def compress(self, chars):
        if not chars:
            return 0
        write_index = 0
        read_index = 0
        length = len(chars)
        while read_index < length:
            char = chars[read_index]
            count = 0
            while read_index < length and chars[read_index] == char:
                read_index += 1
                count += 1
            chars[write_index] = char
            write_index += 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        return write_index