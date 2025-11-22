class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip: str) -> int:
            res = 0
            for part in ip.split('.'):
                res = res * 256 + int(part)
            return res

        def int_to_ip(num: int) -> str:
            return '.'.join(str((num >> (8 * i)) & 255) for i in reversed(range(4)))

        def largest_cidr_size(start: int, n: int) -> int:
            if start & 1 == 1:
                return 1
            x = 1
            while x <= n and start % x == 0:
                x <<= 1
            return x >> 1

        result = []
        start_ip = ip_to_int(ip)

        while n > 0:
            size = largest_cidr_size(start_ip, n)
            cidr_prefix = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{cidr_prefix}")
            start_ip += size
            n -= size

        return result