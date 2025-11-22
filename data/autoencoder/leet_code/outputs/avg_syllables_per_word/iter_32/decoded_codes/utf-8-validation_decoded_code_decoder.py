from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def get_byte_count(byte: int) -> int:
            # Check the pattern of leading bits to determine byte count
            # byte is treated as an 8-bit integer

            # Mask helpers for checking bits
            # Most significant bit (MSB) - bit 7 (from left, zero indexed)
            # 1-byte char: 0xxxxxxx (MSB=0)
            if (byte & 0b10000000) == 0:
                return 1

            # 2-byte char: 110xxxxx (bits 7-5 = 110)
            if (byte & 0b11100000) == 0b11000000:
                return 2

            # 3-byte char: 1110xxxx (bits 7-4 = 1110)
            if (byte & 0b11110000) == 0b11100000:
                return 3

            # 4-byte char: 11110xxx (bits 7-3 = 11110)
            if (byte & 0b11111000) == 0b11110000:
                return 4

            return -1  # Invalid leading byte pattern

        i = 0
        n = len(data)
        while i < n:
            byte_count = get_byte_count(data[i])
            if byte_count == -1:
                return False
            if i + byte_count > n:
                return False
            # For multi-byte character, check continuation bytes
            for j in range(i + 1, i + byte_count):
                # Continuation bytes must start with '10' bits
                if (data[j] & 0b11000000) != 0b10000000:
                    return False
            i += byte_count
        return True