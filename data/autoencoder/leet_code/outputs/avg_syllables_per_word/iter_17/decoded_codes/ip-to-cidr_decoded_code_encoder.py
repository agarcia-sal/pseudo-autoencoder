class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip_address: str) -> int:
            parts = map(int, ip_address.split('.'))
            result = 0
            for part in parts:
                result = result * 256 + part
            return result

        def int_to_ip(number: int) -> str:
            return '.'.join(str((number >> (8 * i)) % 256) for i in range(3, -1, -1))

        def largest_cidr_size(start_value: int, count: int) -> int:
            if start_value & 1 == 1:
                return 1
            x = 1
            while x <= count and (start_value & (x - 1)) == 0:
                x <<= 1
            return x >> 1

        result = []
        start_ip = ip_to_int(ip)

        while n > 0:
            size = largest_cidr_size(start_ip, n)
            prefix_length = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{prefix_length}")
            start_ip += size
            n -= size

        return result