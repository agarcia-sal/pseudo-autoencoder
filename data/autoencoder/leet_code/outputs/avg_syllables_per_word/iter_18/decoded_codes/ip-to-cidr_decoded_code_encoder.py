class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip: str) -> int:
            parts = list(map(int, ip.split('.')))
            result_number = 0
            for part in parts:
                result_number = result_number * 256 + part
            return result_number

        def int_to_ip(num: int) -> str:
            result_string = []
            for i in range(3, -1, -1):
                result_string.append(str((num >> (8 * i)) & 255))
            return '.'.join(result_string)

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
            cidr_len = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{cidr_len}")
            start_ip += size
            n -= size
        return result