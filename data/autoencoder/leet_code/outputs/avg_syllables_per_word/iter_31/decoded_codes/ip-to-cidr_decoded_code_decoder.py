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
            result_parts = []
            for i in range(3, -1, -1):
                shifted_value = num // (256 ** i)
                current_part = shifted_value % 256
                result_parts.append(str(current_part))
            return '.'.join(result_parts)

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
            prefix_length = 32 - (size.bit_length() - 1)
            cidr_string = f"{int_to_ip(start_ip)}/{prefix_length}"
            result.append(cidr_string)
            start_ip += size
            n -= size

        return result