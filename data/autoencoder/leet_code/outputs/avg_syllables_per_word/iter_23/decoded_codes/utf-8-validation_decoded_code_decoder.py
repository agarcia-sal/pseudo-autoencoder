from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_byte_count(byte: int) -> int:
            # Check leading bits for UTF-8 byte count
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
            if byte_count == -1 or i + byte_count > n:
                return False

            # Check that continuation bytes start with '10' bits
            for j in range(i + 1, i + byte_count):
                if (data[j] >> 6) != 0b10:
                    return False
            i += byte_count
        return True