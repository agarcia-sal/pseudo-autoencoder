def validUtf8(data):
    def get_byte_count(b):
        if b >> 7 == 0b0:
            return 1
        elif b >> 5 == 0b110:
            return 2
        elif b >> 4 == 0b1110:
            return 3
        elif b >> 3 == 0b11110:
            return 4
        else:
            return -1

    i = 0
    while i < len(data):
        n = get_byte_count(data[i])
        if n == -1 or i + n > len(data):
            return False
        for j in range(i + 1, i + n):
            if data[j] >> 6 != 0b10:
                return False
        i += n
    return True