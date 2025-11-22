class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip_address: str) -> int:
            parts = list(map(int, ip_address.split('.')))
            result_value = 0
            for part_element in parts:
                result_value = result_value * 256 + part_element
            return result_value

        def int_to_ip(number_value: int) -> str:
            return '.'.join(
                str((number_value >> (8 * i)) % 256) 
                for i in range(3, -1, -1)
            )

        def largest_cidr_size(start_value: int, count_number: int) -> int:
            if start_value & 1 == 1:
                return 1
            x_value = 1
            while x_value <= count_number and (start_value & (x_value - 1)) == 0:
                x_value <<= 1
            return x_value >> 1

        result = []
        start_ip = ip_to_int(ip)

        while n > 0:
            size = largest_cidr_size(start_ip, n)
            prefix_length = 32 - (size.bit_length() - 1)
            result.append(f"{int_to_ip(start_ip)}/{prefix_length}")
            start_ip += size
            n -= size

        return result