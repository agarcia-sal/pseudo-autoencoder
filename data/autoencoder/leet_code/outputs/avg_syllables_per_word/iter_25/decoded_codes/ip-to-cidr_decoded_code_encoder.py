class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip: str) -> int:
            parts = list(map(int, ip.split('.')))
            res = 0
            for part in parts:
                res = res * 256 + part
            return res

        def int_to_ip(num: int) -> str:
            return '.'.join(str((num >> (8 * i)) % 256) for i in reversed(range(4)))

        def largest_cidr_size(start: int, n: int) -> int:
            if start & 1 == 1:
                return 1
            x = 1
            while x <= n and (start & (x - 1)) == 0:
                x *= 2
            return x // 2

        result = []
        start_ip = ip_to_int(ip)
        while n > 0:
            size = largest_cidr_size(start_ip, n)
            mask_len = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{mask_len}")
            start_ip += size
            n -= size
        return result