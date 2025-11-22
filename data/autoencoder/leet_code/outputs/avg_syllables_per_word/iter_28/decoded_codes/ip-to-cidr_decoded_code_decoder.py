from typing import List

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_int(ip: str) -> int:
            parts = list(map(int, ip.split('.')))
            res = 0
            for part in parts:
                res = res * 256 + part
            return res

        def int_to_ip(num: int) -> str:
            list_of_segments = []
            for index in range(3, -1, -1):
                segment_value = (num // (256 ** index)) % 256
                list_of_segments.append(str(segment_value))
            return '.'.join(list_of_segments)

        def largest_cidr_size(start: int, n: int) -> int:
            if start & 1 == 1:
                return 1
            x = 1
            while x <= n and (start & (x - 1)) == 0:
                x <<= 1
            return x >> 1

        result = []
        start_ip = ip_to_int(ip)
        while n > 0:
            size = largest_cidr_size(start_ip, n)
            prefix_len = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{prefix_len}")
            start_ip += size
            n -= size

        return result