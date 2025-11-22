class Solution:
    def validUtf8(self, data):
        def get_byte_count(byte):
            if (byte >> 7) == 0:
                return 1
            elif (byte >> 5) == 0b110:
                return 2
            elif (byte >> 4) == 0b1110:
                return 3
            elif (byte >> 3) == 0b11110:
                return 4
            else:
                return -1

        i = 0
        n = len(data)
        while i < n:
            byte_count = get_byte_count(data[i])
            if byte_count == -1:
                return False
            if i + byte_count > n:
                return False
            for j in range(i + 1, i + byte_count):
                if (data[j] >> 6) != 0b10:
                    return False
            i += byte_count

        return True